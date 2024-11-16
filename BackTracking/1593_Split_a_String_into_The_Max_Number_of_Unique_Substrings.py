class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        return self.dfs(s, 0, set())
    
    def dfs(self, s, start, hashset):
        if start == len(s):
            return len(hashset)
        count = 0
        for i in range(start + 1, len(s) + 1):
            subS = s[start: i]
            if subS not in hashset:
                hashset.add(subS)
                count = max(count, self.dfs(s, i, hashset))
                hashset.remove(subS)
        return count