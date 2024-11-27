# EC: empty arr?, -ve nums?, maxLen of arr?, num range?, multiple sums?, target less than min sum?
"""
[2,7,11,15]
 l       r
 2 + 15? more
 2 + 11? more
 2 + 7 ? found
"""
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # initialize two pointers left and right
        left, right = 0, len(numbers) - 1
        # continue till left and right cross each other
        while left < right:
            total = numbers[left] + numbers[right]
            # if sum is more move right pointer towards left
            if total > target:
                right -= 1 
            # if sum is less move left pointer towards right
            elif total < target:
                left += 1
            # if they are equal return result
            else:
                return [left + 1, right + 1]
        # return empty if not found anything
        return []
# TC: O(n) -> every element is checked at most once
# SC: O(1) -> left, right pointers and total (O(1))