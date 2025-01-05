# EC: empty string?, single char?, case sensitive?, handle non alphabets?, shift with 0?
class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        """
        abcdefghijklmnopqrstuvwxyz
        s = "abc"
        shifts = [3,5,9]
        dbc (3) a -> d
        igc (5) d -> i, b -> g
        rpl (9) i -> r, 
        """
        result, shift = "", 0
        for i in range(len(shifts) - 1, -1, -1):
            result += chr((ord(s[i]) - ord('a') + shift + shifts[i]) % 26 + ord('a'))
            shift += shifts[i]
        return result[::-1]
# TC: O(n) -> Single reverse iteration through the input string and shifts array
# SC: O(n) -> result string will be same size as s

