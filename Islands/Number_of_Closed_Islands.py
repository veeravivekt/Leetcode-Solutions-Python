class Solution:
  def countClosedIslands(self, matrix):
    countClosedIslands = 0
    # TODO: Write your code here
    rows = len(matrix)
    cols = len(matrix[0])
    visited = [[False for i in range(cols)] for j in range(rows)]
    for i in range(rows):
      for j in range(cols):
        if matrix[i][j] == 1 and not visited[i][j]:
          if self.dfs(matrix, i, j, visited):
            countClosedIslands += 1
    return countClosedIslands 

  def dfs(self, matrix, x, y, visited):
    if x < 0 or x >= len(matrix) or y < 0 or y >= len(matrix[0]):
      return False
    if matrix[x][y] == 0 or visited[x][y]:
      return True
    visited[x][y] = True
    closed = True
    closed &= self.dfs(matrix, x - 1, y, visited)
    closed &= self.dfs(matrix, x + 1, y, visited)
    closed &= self.dfs(matrix, x, y - 1, visited)
    closed &= self.dfs(matrix, x, y + 1, visited)
    return closed