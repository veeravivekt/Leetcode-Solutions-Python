# Edge Cases: Empty array, same nums, no match
# Clarifying Questions: expected range of nums?, max size of arr?
"""
[1,2,3,1,1,3]
 0 1 2 3 4 5
pairs = 0,3 0,4 2,5 3,4
count = 2 + 0 + 1 + 1 + 0 + 0
 1 : 3
 2 : 1
 3 : 2
"""
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        result = 0
        # count all numbers and store in a dict
        store = {}
        for n in nums:
            store[n] = store.get(n, 0) + 1
        # iterate each number from nums
        for n in nums:
            # subtract 1 from its count
            store[n] -= 1
            # add rest of the count to result
            result += store[n]
        # return answer
        return result
# TC: O(n) -> counting nums(O(n)) + iterate each num(O(n))
# SC: O(n) -> store O(n worst case if all are unique)