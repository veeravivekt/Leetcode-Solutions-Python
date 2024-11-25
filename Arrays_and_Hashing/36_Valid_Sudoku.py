class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # initialize 3 sets for row, col and each subbox
        rows = defaultdict(set)
        cols = defaultdict(set)
        subbox = defaultdict(set)
        # check every row and column of sudoku board 9 * 9
        for r in range(9):
            for c in range(9):
                cell = board[r][c]
                # if cell is not filled skip
                if cell == '.':
                    continue
                # check current number is already there in sets
                if cell in rows[r] \
                    or cell in cols[c] \
                    or cell in subbox[r // 3, c // 3]:
                    return False
                # add the current element to all sets
                rows[r].add(cell)
                cols[c].add(cell)
                subbox[r // 3, c // 3].add(cell)
        # return True if it is valid
        return True
# TC: O(n**2) -> if we generalize len of board(O(n**2)), but it is O(1) as it has 81 itr
# SC: O(n**2) -> same