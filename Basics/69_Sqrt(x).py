class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        while l <= r:
            m = l + (r - l) // 2
            n = m * m
            if n > x:
                r = m - 1
            elif n < x:
                l = m + 1
            else:
                return m
        return r