class Solution:
    def minWindow(self, s: str, t: str) -> str:
        k = len(t)
        mapT = {}
        for c in t:
            mapT[c] = mapT.get(c, 0) + 1
        left = 0
        matched = 0
        minLen = len(s) + 1
        subStr = 0
        for right in range(len(s)):
            if s[right] in mapT:
                mapT[s[right]] -= 1
                if mapT[s[right]] == 0:
                    matched += 1
            while matched == len(mapT):
                if right - left + 1 < minLen:
                    minLen = right - left + 1
                    subStr = left
                if s[left] in mapT:
                    if mapT[s[left]] == 0:
                        matched -= 1
                    mapT[s[left]] += 1
                left += 1
        return "" if minLen > len(s) else s[subStr: subStr + minLen]