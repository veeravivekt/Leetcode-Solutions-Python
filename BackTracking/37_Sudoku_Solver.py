class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.solve(board)
    
    def solve(self, board):
        for row in range(9):
            for col in range(9):
                if board[row][col] == '.':
                    for n in range(1, 10):
                        if self.isValid(board, row, col, str(n)):
                            board[row][col] = str(n)
                            if self.solve(board):
                                return True
                            else:
                                board[row][col] = '.'
                    return False
        return board
    
    def isValid(self, board, row, col, n):
        for i in range(9):
            if board[row][i] == n:
                return False
            if board[i][col] == n:
                return False
            if board[(row // 3) * 3 + i // 3][(col // 3) * 3 + i % 3] == n:
                return False
        return True 