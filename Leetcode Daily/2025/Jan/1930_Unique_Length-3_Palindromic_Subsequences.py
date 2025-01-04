# EC: size of string can be less than 3?, max size of s?, casesenstive?, only alpha?
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        letters = set(s)
        count = 0
        for letter in letters:
            i, j = s.index(letter), s.rindex(letter)
            middleElements = set()
            
            for i in range(i + 1, j):
                middleElements.add(s[i])
            count += len(middleElements)
        return count
# TC: O(k * n) - Iterates over each unique character (k) and potentially scans the entire string (n) for each.
# SC: O(k) - Stores sets of unique characters, where k is the number of unique characters in the string.
