# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        minDepth = 0
        if not root:
            return minDepth
        queue = []
        queue.append(root)
        while queue:
            minDepth += 1
            size = len(queue)
            for _ in range(size):
                currentNode = queue.pop(0)
                if not currentNode.left and not currentNode.right:
                    return minDepth
                if currentNode.left:
                    queue.append(currentNode.left)
                if currentNode.right:
                    queue.append(currentNode.right)
        