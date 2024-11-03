class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        x1 = 0
        for n in nums:
            x1 ^= n
        return x1
