class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        rows = len(grid)
        cols = len(grid[0])
        visited = [[False for i in range(cols)]for j in range(rows)]
        for i in range(rows):
            for j in range(cols):
                if not visited[i][j]:
                    if self.dfs(grid, i, j, grid[i][j], -1, -1, visited):
                        return True
        return False
    
    def dfs(self, grid, x, y, value, prevX, prevY, visited):
        if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
            return False
        if grid[x][y] != value:
            return False
        if visited[x][y]:
            return True
        visited[x][y] = True
        if x - 1 != prevX and self.dfs(grid, x - 1, y, value, x, y, visited):
            return True
        if x + 1 != prevX and self.dfs(grid, x + 1, y, value, x, y, visited):
            return True
        if y - 1 != prevY and self.dfs(grid, x, y - 1, value, x, y, visited):
            return True
        if y + 1 != prevY and self.dfs(grid, x, y + 1, value, x, y, visited):
            return True
        return False