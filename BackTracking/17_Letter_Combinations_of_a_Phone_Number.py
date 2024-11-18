# BackTracking TC: O(n * 4^n) SC: O(n)
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        buttons = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz"
        }
        
        result = []
        def backtrack(i, currS):
            if len(currS) == len(digits):
                result.append(currS)
                return
            for c in buttons[digits[i]]:
                backtrack(i + 1, currS + c)
        if digits:
            backtrack(0, "")
        
        return result