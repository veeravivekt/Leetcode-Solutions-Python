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