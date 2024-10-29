# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        allPaths = []
        self.dfs(root, targetSum, [], allPaths)
        return allPaths
    def dfs(self, root, targetSum, currentPath, allPaths):
        if root is None:
            return
        currentPath.append(root.val)
        if root.val == targetSum and root.left is None and root.right is None:
            allPaths.append(list(currentPath))
        else:
            self.dfs(root.left, targetSum - root.val, currentPath, allPaths)
            self.dfs(root.right, targetSum - root.val, currentPath, allPaths)
        currentPath.pop(-1)