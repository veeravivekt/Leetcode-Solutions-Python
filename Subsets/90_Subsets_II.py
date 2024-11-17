class Solution:
    def subsetsWithDup(self, nums):
        nums.sort()
        subsets = [[]]
        end = 0
        for i in range(len(nums)):
            start = 0
            if i > 0 and nums[i] == nums[i - 1]:
                start = end
            end = len(subsets)
            for j in range(start, end):
                miniSet = list(subsets[j])
                miniSet.append(nums[i])
                subsets.append(miniSet)
        return subsets

# BackTracking TC: O(n * 2^n) SC: O(n)
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = set()
        def backtrack(i, subset):
            if i == len(nums):
                result.add(tuple(subset))
                return
            subset.append(nums[i])
            backtrack(i + 1, subset)
            subset.pop()
            backtrack(i + 1, subset)
        nums.sort()
        backtrack(0, [])
        return [list(s) for s in result]