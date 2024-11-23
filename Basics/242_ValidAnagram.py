# TC: O(n) -> each character from each strings is checked atmost once
# SC: O(1) -> charStore(O(26)), i(O(1))
# Edge Cases: Empty Strings, Diff Lengths, case sensitive, size of strings, non Alpha
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Basecase: if lenths are diff return False
        if len(s) != len(t):
            return False
        # initialize a charStores
        charStore = [0] * 26
        # for each character in both s and t
        for i in range(len(s)):
            # add 1 to charStore for each char in s
            charStore[ord(s[i]) - ord('a')] += 1
            # subtract 1 to charStore for each char in s
            charStore[ord(t[i]) - ord('a')] -= 1
        # if everything is 0 in charStore return True
        for n in charStore:
            if n != 0:
                return False
        return True