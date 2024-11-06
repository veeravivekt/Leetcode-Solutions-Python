class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        balance, count = 0, 0
        for c in s:
            if c == "(":
                balance += 1
            else:
                balance -= 1
            
            if balance == -1:
                count += 1
                balance += 1
        return count + balance