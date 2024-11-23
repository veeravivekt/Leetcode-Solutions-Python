# Edge Cases: empty strings, diff Lengths, case sensitive, size of strings, non-alpha
"""
s = "anagram", t = "nagaram"
     0  1  2  3  4  5  6
a = 1 + 1 + 1 - 1 - 1 - 1 = 0
n = 1 - 1 = 0
g = 1 - 1 = 0
r = 1 - 1 = 0
m = 1 - 1 = 0
"""
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
# TC: O(n) -> each character from each strings is checked atmost once
# SC: O(1) -> charStore(O(26)), i(O(1))



# Follow up: Unicode Characters
# hashmap would be more suitable for these situations
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if lengths are diff return false
        if len(s) != len(t):
            return False
        # intialize a hashmap to store count of unicode chars
        charStore = {}
        # iterate throught all chars of s and t
        for i in range(len(s)):
            # add count to charStore for s
            charStore[s[i]] = charStore.get(s[i], 0) + 1
            # subtract count to charStore for t
            charStore[t[i]] = charStore.get(t[i], 0) - 1
        # verify if all values in charStore are 0
        for v in charStore.values():
            if v != 0:
                return False
        return True
# TC: O(n) -> every char is checked atmost once O(n) + every value in charStore (O(26))
# SC: O(n) -> charStore for n unique chars