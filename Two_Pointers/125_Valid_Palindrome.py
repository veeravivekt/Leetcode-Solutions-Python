# Approach: Two Pointers
# TC: O(n) -> each char is checked at most once
# SC: O(1) -> left, right
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # initialize two pointers left and right
        left, right = 0, len(s) - 1
        # continue till they cross over
        while left < right:
            # while not alnum increment left
            while left < right and not s[left].isalnum():
                left += 1
            # while not alnum increment right
            while left < right and not s[right].isalnum():
                right -= 1
            # compare if left and right are equal after converting to lowercase
            if s[left].lower() != s[right].lower():
                return False
            # move pointers
            left += 1
            right -= 1
        # return true if all characters matches and loop ends
        return True