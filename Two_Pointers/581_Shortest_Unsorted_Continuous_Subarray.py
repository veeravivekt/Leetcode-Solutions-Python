class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < len(nums) - 1 and nums[left] <= nums[left + 1]:
            left += 1
        if left == len(nums) - 1:
            return 0
        while right > 0 and nums[right] >= nums[right - 1]:
            right -= 1
        
        minSub = math.inf
        maxSub = -math.inf
        for i in range(left, right + 1):
            minSub = min(minSub, nums[i])
            maxSub = max(maxSub, nums[i])

        while left > 0 and nums[left - 1] > minSub:
            left -= 1
        while right < len(nums) - 1 and nums[right + 1] < maxSub:
            right += 1
        return right - left + 1