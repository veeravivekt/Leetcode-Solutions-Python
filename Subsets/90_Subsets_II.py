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