class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charStore = {}
        maxChars, maxLen = 0, 0
        left = 0
        for right in range(len(s)):
            charStore[s[right]] = charStore.get(s[right], 0) + 1
            maxChars = max(maxChars, charStore[s[right]])
            if (right - left + 1) - maxChars > k:
                charStore[s[left]] -= 1
                left += 1
            maxLen = max(maxLen, right - left + 1)
        return maxLen