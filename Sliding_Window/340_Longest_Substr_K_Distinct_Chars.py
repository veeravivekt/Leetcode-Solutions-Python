class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if k == 0: return 0
        hashmap = {}
        left = 0
        longest = -math.inf
        for right in range(len(s)):
            hashmap[s[right]] = hashmap.get(s[right], 0) + 1
            if len(hashmap) > k:
                hashmap[s[left]] -= 1
                if hashmap[s[left]] == 0: hashmap.pop(s[left])
                left += 1
            longest = max(longest, right - left + 1)
        return longest
            