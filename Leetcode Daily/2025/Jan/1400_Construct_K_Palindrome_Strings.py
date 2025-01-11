class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        # if length is below k then you cant form k palindrome strings
        if len(s) < k:
            return False
        # if exactly equal to k then each individual char is palindrome
        if len(s) == k:
            return True
        
        # count all characters
        charStore = [0] * 26
        for c in s:
            charStore[ord(c) - ord('a')] += 1
        
        # count all odd char freq
        odd = 0
        for count in charStore:
            if count % 2 == 1:
                odd += 1
        return odd <= k
# TC: O(n) = traverse throught string once O(n)
# SC: O(1) = charStore O(26)