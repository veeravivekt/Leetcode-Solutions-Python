class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        map = {}
        count = 0
        for n in nums:
            map[n] = map.get(n, 0) + 1
            count += map[n] - 1
        return count