# EC: Empty?, Negative Values?, Multiple occurences of num?, maxLen of nums?, range?
"""
[100,4,200,1,3,2]
100 - 1? = no -> 100
4 - 1? = yes -> skip
200 - 1? = no -> 200
1 - 1? = no -> 1, 2, 3, 4
2 - 1? = yes -> skip
3 - 1? = yes -> skip
4 - 1? = yes -> skip
"""
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # add values to set for constant lookup time
        store = set(nums)
        # have a variable to track the longest consective sequence
        result = 0
        # iterate throught each and every num
        for n in nums:
            # check if we have a num before the current num if yes skip
            if (n - 1) in store:
                continue
            # if not check how long can it extend
            length = 1
            while (n + 1) in store:
                n += 1
                length += 1
            result = max(result, length)
        # return the longest sequence
        return result
# TC: O(n) Each element is processed at most twice, resulting in linear time complexity.
# SC: O(n) The set potentially stores all unique elements from the input list.