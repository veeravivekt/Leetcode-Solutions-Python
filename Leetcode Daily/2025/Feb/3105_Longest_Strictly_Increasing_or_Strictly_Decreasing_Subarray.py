class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        max_len = increase_len = decrease_len = 1
        for i in range(len(nums) - 1):
            if nums[i + 1] > nums[i]:
                increase_len += 1
                decrease_len = 1
            elif nums[i + 1] < nums[i]:
                increase_len = 1
                decrease_len += 1
            else:
                increase_len = decrease_len = 1
            max_len = max(max_len, increase_len, decrease_len)
        return max_len