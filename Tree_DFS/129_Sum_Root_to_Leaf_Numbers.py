# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root, 0)
    def dfs(self, root, pathSum):
        if not root:
            return 0
        pathSum = pathSum * 10 + root.val
        if root.left is None and root.right is None:
            return pathSum
        return self.dfs(root.left, pathSum) + self.dfs(root.right, pathSum)