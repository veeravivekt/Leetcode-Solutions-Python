class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        subsets.append([])
        for n in nums:
            currentSize = len(subsets)
            for i in range(currentSize):
                currentSet = list(subsets[i])
                currentSet.append(n)
                subsets.append(currentSet)
        return subsets
    
# BackTracking
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        subset = []
        def dfs(i):
            if i >= len(nums):
                result.append(list(subset))
                return
            subset.append(nums[i])
            dfs(i + 1)
            subset.pop()
            dfs(i + 1)
        dfs(0)
        return result