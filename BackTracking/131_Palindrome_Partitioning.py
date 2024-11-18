# BackTracking TC: O(n * 2^n) SC: O(n)
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        return self.backtrack(s, 0, [], [])
    
    def backtrack(self, s, i, part, result):
        if i >= len(s):
            result.append(list(part))
            return
        for j in range(i, len(s)):
            if self.isPalindrome(s, i, j):
                part.append(s[i: j + 1])
                self.backtrack(s, j + 1, part, result)
                part.pop()
        return result
    
    def isPalindrome(self, s, i, j):
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True