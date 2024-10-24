class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 1
        i = 0
        while i < len(nums):
            if nums[count - 1] != nums[i]:
                nums[count] = nums[i]
                count += 1
            i += 1
        return count