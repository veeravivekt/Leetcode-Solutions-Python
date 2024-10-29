# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        hashmap = {}
        return self.dfs(root, targetSum, hashmap, 0)
    def dfs(self, root, targetSum, hashmap, currentSum):
        if root is None:
            return 0
        pathCount = 0
        currentSum += root.val
        if currentSum == targetSum:
            pathCount += 1
        pathCount += hashmap.get(currentSum - targetSum, 0)
        hashmap[currentSum] = hashmap.get(currentSum, 0) + 1
        pathCount += self.dfs(root.left, targetSum, hashmap, currentSum)
        pathCount += self.dfs(root.right, targetSum, hashmap, currentSum)
        hashmap[currentSum] -= 1
        return pathCount