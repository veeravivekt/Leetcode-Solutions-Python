# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxSum = -math.inf
        self.dfs(root)
        return self.maxSum
    def dfs(self, root):
        if root is None:
            return 0
        maxLeft = max(self.dfs(root.left), 0)
        maxRight = max(self.dfs(root.right), 0)
        currentSum = maxLeft + maxRight + root.val
        self.maxSum = max(self.maxSum, currentSum)
        return max(maxLeft, maxRight) + root.val