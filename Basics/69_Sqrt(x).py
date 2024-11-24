# EC: range of x?, negative x?, perfect vs non perfect sqrs?, overflow?
class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        # initalize the range to search for sqrt
        left, right = 2, x // 2
        # search till left and right cross each other
        while left <= right:
            # caliculate mid value
            mid = left + (right - left) // 2
            square = mid * mid
            # set left as mid + 1 if its less
            if square < x:
                left = mid + 1
            # set right as mid - 1 if its more
            elif square > x:
                right = mid - 1
            else:
                return mid   
        # return right
        return right
# TC: O(logn) -> binary search each time search space is halfed
# SC: O(1) -> left, right (O(1))