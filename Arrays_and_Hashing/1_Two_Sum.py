# EC: empty array?, target less than min sum?, multiple ans?
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # have a hashmap to store passed elements
        store = {}
        # verify every element
        for i, n in enumerate(nums):
            # check if target - num is present in hashmap
            diff = target - n
            if diff in store:
                return [store[diff], i]
            store[n] = i
# TC: O(n) -> each num is checked at most once
# SC: O(n) -> store can have max of n unique nums