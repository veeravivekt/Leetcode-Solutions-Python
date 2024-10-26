class Solution:
  def findPermutation(self, str1, pattern):
    patternMap = {}
    for p in pattern:
      patternMap[p] = patternMap.get(p, 0) + 1
    
    left = 0
    strMap = {}
    for right in range(len(str1)):
      strMap[str1[right]] = strMap.get(str1[right], 0) + 1
      if right - left + 1 > len(pattern):
        strMap[str1[left]] -= 1
        if strMap[str1[left]] == 0: strMap.pop(str1[left])
        left += 1
      if strMap == patternMap:
        return True
    return False