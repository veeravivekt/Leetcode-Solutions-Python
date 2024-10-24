class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        l, r = 0, n - 1
        highestSquare = n - 1
        squares = [0 for i in range(n)]
        while l <= r:
            lSquare = nums[l] ** 2
            rSquare = nums[r] ** 2
            if lSquare > rSquare:
                squares[highestSquare] = lSquare
                l += 1
            else:
                squares[highestSquare] = rSquare
                r -= 1
            highestSquare -= 1
        return squares