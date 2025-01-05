# EC: empty string?, single char?, case sensitive?, handle non alphabets?, shift with 0?
class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        shift = [0] * (n + 1)
        for start, end, direction in shifts:
            shift[start] += (1 if direction == 1 else -1)
            if end + 1 < n:
                shift[end + 1] -= (1 if direction == 1 else -1)
        result = list(s)
        currShift = 0
        for i in range(n):
            currShift += shift[i]
            result[i] = chr((ord(result[i]) - ord('a') + currShift) % 26 + ord('a'))
        return "".join(result)
# TC: O(n + m) -> process shifts O(m), apply final shifts O(n)
# SC: O(n) -> shift array

