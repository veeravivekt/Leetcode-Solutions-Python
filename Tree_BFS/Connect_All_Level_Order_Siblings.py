#class TreeNode:
#  def __init__(self, val):
#    self.val = val
#    self.left, self.right, self.next = None, None, None


class Solution:
  def connect(self, root):
    # TODO: Write your code here
    if not root:
      return
    queue = []
    queue.append(root)
    prevNode = None
    while queue:
      size = len(queue)
      for _ in range(size):
        currentNode = queue.pop(0)
        if prevNode:
          prevNode.next = currentNode
        prevNode = currentNode
        if currentNode.left:
          queue.append(currentNode.left)
        if currentNode.right:
          queue.append(currentNode.right)
    return root

