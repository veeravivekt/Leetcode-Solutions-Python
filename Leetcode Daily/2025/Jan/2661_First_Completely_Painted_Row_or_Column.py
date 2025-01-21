class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        """
        arr = [1,3,4,2]
        mat = [[1,4],[2,3]]
        rowCount = [2, 1]
        colCount = [1, 2]
        1 -> 0, 0
        3 -> 1, 1
        4 -> 0, 1 (rowCount == cols return index)
        """
        rows, cols = len(mat), len(mat[0])
        rowCount, colCount = [0] * rows, [0] * cols
        posMap = defaultdict(list)
        for r in range(rows):
            for c in range(cols):
                posMap[mat[r][c]] = [r, c]
        for i, n in enumerate(arr):
            currRow, currCol = posMap[n]
            rowCount[currRow] += 1
            colCount[currCol] += 1
            print(rowCount, colCount)
            if rowCount[currRow] == cols or colCount[currCol] == rows:
                return i
        return -1
# TC: O(m * n) = assign values to posMap O(m * n) + worst case check all nums in arr O(m * n)
# SC: O(m * n) = posMap stores O(m * n) + rowCount, colCount both stores O(m + n)