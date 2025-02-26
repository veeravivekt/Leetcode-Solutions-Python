"""
nums = [1,-3,2,3,-4]
[1, -3, 2, 3, -4]
Prefix sum:
[1, -3, 2, 3, -4]
 ^
 prefixSum = 0 + 1 = 1 (min = 1, max = 1)
[1, -3, 2, 3, -4]
     ^
 prefixSum = 1 + (-3) = -2 (min = -2, max = 1)
[1, -3, 2, 3, -4]
        ^
prefixSum = -2 + 2 = 0 (min = -2, max = 1)
[1, -3, 2, 3, -4]
           ^
prefixSum = 0 + 3 = 3 (min = -2, max = 3)
[1, -3, 2, 3, -4]
               ^
prefixSum = 3 + (-4) = -1 (min = -2, max = 3)

Absoluete Sum = max - min = 3 - (-2) = 5
"""
class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        # initalize min and max prefix sum
        minPrefixSum = 0
        maxPrefixSum = 0
        # calculate each prefix sum
        prefixSum = 0
        for n in nums:
            # find the min and max prefix sum for each
            prefixSum += n
            minPrefixSum = min(minPrefixSum, prefixSum)
            maxPrefixSum = max(maxPrefixSum, prefixSum)
        return maxPrefixSum - minPrefixSum
# TC: O(n) -> Going through nums array only once and caliculating min and max which are all O(1) for n nums
# SC: O(1) -> min, max and prefixSum all are O(1)