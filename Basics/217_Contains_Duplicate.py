# EC: empty?, maxLength of nums?, how big is each number?
"""
[1, 2, 3, 1]
          n
set = 1, 2, 3
"""
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # initialize a set to keep track of seen nums
        hashset = set()
        # check each number in nums
        for n in nums:
            # if number is already in set return True
            if n in hashset:
                return True
            # add number to set
            hashset.add(n)
        # return False if no duplicate
        return False
# TC: O(n) -> each number is checked at most once
# SC: O(n) -> hashset is filled with n unique nums worst case
