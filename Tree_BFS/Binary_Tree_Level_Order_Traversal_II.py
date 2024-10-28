# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = deque()
        if root is None:
            return []
        queue = deque()
        queue.append(root)
        while queue:
            size = len(queue)
            currentLevel = []
            for _ in range(size):
                currentNode = queue.popleft()
                currentLevel.append(currentNode.val)
                if currentNode.left:
                    queue.append(currentNode.left)
                if currentNode.right:
                    queue.append(currentNode.right)
            result.appendleft(currentLevel)
        result = [list(sublist) for sublist in result]
        return result