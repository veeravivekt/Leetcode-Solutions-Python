# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        if not root:
            return result
        queue = []
        queue.append(root)
        zigzag = False
        while queue:
            size = len(queue)
            currentLevel = deque()
            childs = []
            for _ in range(size):
                currentNode = queue.pop(0)
                if zigzag:
                    currentLevel.appendleft(currentNode.val)
                else:
                    currentLevel.append(currentNode.val)
                if currentNode.left:
                    queue.append(currentNode.left)
                if currentNode.right:
                    queue.append(currentNode.right)
            result.append(list(currentLevel))
            zigzag = not zigzag
        return result