class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        """
        [10,20,30,5,10,50]
        10 -> 20 -> 30 break 5 -> 10 -> 50
        """
        max_sum = subarr_sum = nums[0]
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                subarr_sum += nums[i]
                max_sum = max(max_sum, subarr_sum)
            else:
                subarr_sum = nums[i]
        return max_sum
# TC: O(n) -> Iterating all elements once
# SC: O(1) -> max_sum, subarr_sum and i (all are O(1))