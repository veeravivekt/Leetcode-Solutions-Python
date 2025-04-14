# EC: empty, single element, All -ve or +ve nums, array with 0, array with only 0's, duplicate nums, Array with max or min values
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        """
        [-4,-1,0,3,10]
            ^    ^
        -4 or 10 -> 10
        -4 or 3 -> -4
        -1 or 3 -> 3
        -1 or 0 -> -1
        0 -> 0
        """
        # initialzie a result array and pos
        sortedArr = [0] * len(nums)
        pos = len(nums) - 1
        left, right = 0, len(nums) - 1
        # run a while loop until left > right
        while left <= right:
            # check which abs value is greater between left and right pointers
            # if left is greater then assign its square to pos in array
            if abs(nums[left]) > abs(nums[right]):
                sortedArr[pos] = nums[left] ** 2
                left += 1
            # if right is greater do the same
            else:
                sortedArr[pos] = nums[right] ** 2
                right -= 1
            pos -= 1
        # return array
        return sortedArr
# TC: O(n) -> each number is being iterated once
# SC: O(n) -> sortedArr -> O(n), pos|left|right -> O(1)