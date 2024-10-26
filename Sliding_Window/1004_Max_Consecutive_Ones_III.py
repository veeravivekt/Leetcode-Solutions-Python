class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        m = {0 : 0, 1 : 0}
        left = 0
        maxArr = 0
        for right in range(len(nums)):
            m[nums[right]] += 1
            while m[0] > k:
                m[nums[left]] -= 1
                left += 1
            maxArr = max(maxArr, right - left + 1)
        return maxArr