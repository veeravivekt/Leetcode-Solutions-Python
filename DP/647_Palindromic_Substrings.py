# Two Pointers
class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        for i in range(len(s)):
            count += self.helper(i, i, s)
            count += self.helper(i, i + 1, s)
        return count
    def helper(self, l, r, s):
        subCount = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            subCount += 1
            l -= 1
            r += 1
        return subCount
    
# DP - Bottom Up
class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        n = len(s)
        dp = [[False] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i <= 2 or dp[i + 1][j - 1]):
                    count += 1
                    dp[i][j] = True
        return count