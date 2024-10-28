# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        result = []
        if not root:
            return result
        queue = []
        queue.append(root)
        while queue:
            size = len(queue)
            sumOfLevel = 0
            for _ in range(size):
                currentNode = queue.pop(0)
                sumOfLevel += currentNode.val
                if currentNode.left:
                    queue.append(currentNode.left)
                if currentNode.right:
                    queue.append(currentNode.right)
            result.append(round(sumOfLevel / size, 5))
        return result