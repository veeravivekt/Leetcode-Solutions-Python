# EC: Empty s?, All 0's or 1's, Len of s, s have only 1 or 0?
class Solution:
    def maxScore(self, s: str) -> int:
        """
        011101
        1 -> 0 11101
        2 -> 01 1101
        3 -> 011 101
        4 -> 0111 01
        5 -> 01110 1
        """
        result, zeros = 0, 0
        ones = s.count("1")

        for i in range(len(s) - 1):
            zeros += s[i] == '0'
            ones -= s[i] == '1'
            result = max(result, zeros + ones)
        return result
# TC: O(n) due to one pass through the string
# SC: O(1) as it uses only a constant amount of extra space