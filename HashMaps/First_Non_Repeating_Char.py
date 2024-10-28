class Solution:
    def firstUniqChar(self, s: str) -> int:
        # ToDo: Write Your Code Here.
        hashmap = {}
        for c in s:
            hashmap[c] = hashmap.get(c, 0) + 1
        for i in range(len(s)):
            if hashmap[s[i]] == 1:
                return i
        return -1

