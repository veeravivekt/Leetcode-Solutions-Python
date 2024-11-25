# EC: maxlen of nums?, range of each num?, negative nums?, zero?, all ones?
"""
nums = 
[1,2,3,4]
-> [1, 1, 2, 6]
1 * 1, 1 * 2, 2 * 3
[24 * 1, 12 * 1, 4 * 2, 6]<-
1 * 4, 4 * 3, 12 * 2
[24, 12, 8, 6]
"""
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # initiate a array with all zeros with sam len as nums
        result = [0] * len(nums)
        # take prod and intiate to 1
        prod = 1
        # iterate each num and update prod value to it
        for i in range(len(nums)):
            result[i] = prod
        # multiply prod with nums[i]
            prod *= nums[i]

        # take a new prod value to 1
        prod = 1
        # iterate each num from back
        for i in range(len(nums) - 1, -1, -1):
        # multiply prod value to the current num
            result[i] *= prod
        # multiply prod value with nums[i]
            prod *= nums[i]
        return result

# TC: O(n) -> all elements of nums are checked twice O(n) + O(n) = O(n)
# SC: O(n) -> result stores size equal to nums