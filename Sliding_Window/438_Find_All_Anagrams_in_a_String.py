class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        indexs = []
        left = 0
        mapP = {}
        for c in p:
            mapP[c] = mapP.get(c, 0) + 1
        mapS = {}
        for right in range(len(s)):
            mapS[s[right]] = mapS.get(s[right], 0) + 1
            if right - left + 1 > len(p):
                mapS[s[left]] -= 1
                if mapS[s[left]] == 0: mapS.pop(s[left])
                left += 1
            if mapS == mapP:
                indexs.append(left)
        return indexs