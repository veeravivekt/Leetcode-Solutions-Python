# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        result = []
        queue = []
        queue.append(root)
        while queue:
            size = len(queue)
            for _ in range(size):
                currentNode = queue.pop(0)
                if currentNode.left:
                    queue.append(currentNode.left)
                if currentNode.right:
                    queue.append(currentNode.right)
                if _ == size - 1:
                    result.append(currentNode.val)
        return result
