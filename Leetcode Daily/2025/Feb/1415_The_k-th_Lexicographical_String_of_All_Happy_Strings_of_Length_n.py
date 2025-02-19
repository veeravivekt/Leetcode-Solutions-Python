class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        """
        consits only ['a', 'b', 'c']
        s[i] != s[i + 1]
        n = 3
        a               b               c
        ab  ac          ba bc           ca cb
        aba abc aca acb bab bac bca bcb cab cac cba cbc
        """
        happyStrings = []
        self.buildHappyStrings("", happyStrings, n)
        if len(happyStrings) < k:
            return ""
        return happyStrings[k - 1]
    
    def buildHappyStrings(self, currStr, happyStrings, n):
        if len(currStr) == n:
            happyStrings.append(currStr)
            return
        for a in ['a', 'b', 'c']:
            if not currStr or currStr[-1] != a:
                self.buildHappyStrings(currStr + a, happyStrings, n)
# TC: O(2^n) - Generates all 3 * 2^(n-1) happy strings recursively, simplified to 2^n for big O notation.
# SC: O(2^n) - Stores all 3 * 2^(n-1) generated happy strings in a list, dominating the O(n) recursion stack.