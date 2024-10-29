#class TreeNode:
#  def __init__(self, val, left=None, right=None):
#    self.val = val
#    self.left = left
#    self.right = right

class Solution:
  def findPath(self, root, sequence):
    # TODO: Write your code here
    return self.dfs(root, sequence, 0)
  
  def dfs(self, root, sequence, index):
    if root is None:
      return False
    if index >= len(sequence) or root.val != sequence[index]:
      return False
    if root.left is None and root.right is None:
      return index == len(sequence) - 1
    return self.dfs(root.left, sequence, index + 1) or self.dfs(root.right, sequence, index + 1)
