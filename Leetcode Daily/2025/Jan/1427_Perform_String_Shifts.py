# EC: shifts more than len of s?, alpha only?, caseSenstive?, max len of str?, leftshift = rightshift
class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        """
        s = "abcdefg"
        shift = [[1,1],[1,1],[0,2],[1,3]]
        [1, 1] : "abcdefg" -> "gabcdef"
        [1, 1] : "gabcdef" -> "fgabcde"
        [0, 2] : "fgabcde" -> "abcdefg"
        [1, 3] : "abcdefg" -> "efgabcd"
        
        Simplification:
        [[1,1],[1,1],[0,2],[1,3]]
        simplify = - 1 - 1 + 2 - 3 = - 3
        "efgabcd"
        """
        simplify = 0
        for direction, amount in shift:
            simplify += amount if direction == 1 else -amount
        simplify %= len(s) # if simplify value is more than length
        return s[-simplify:] + s[:-simplify]
# TC: O(m + n) = O(m) number of shift operations + O(n) lenth of string(slicing string)
# SC: O(n) = slicing creates a new string