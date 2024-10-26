class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minLen = math.inf
        left = 0
        sum = 0
        for right in range(len(nums)):
            sum += nums[right]
            print(sum)
            while sum >= target:
                minLen = min(minLen, right - left + 1)
                sum -= nums[left]
                left += 1
        return 0 if minLen == math.inf else minLen