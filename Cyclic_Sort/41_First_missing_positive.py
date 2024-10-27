class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i, n = 0, len(nums)
        while i < n:
            j = nums[i] - 1
            if nums[i] > 0 and nums[i] <= n and nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1
        for i in range(n):
            if i + 1 != nums[i]:
                return i + 1
        return n + 1