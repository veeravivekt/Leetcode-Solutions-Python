class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = [[False for i in range(cols)]for j in range(rows)]
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and not visited[i][j]:
                    return self.dfs(grid, i, j, visited)   
        return 0
    
    def dfs(self, grid, x, y, visited):
        if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
            return 1
        if grid[x][y] == 0:
            return 1
        if visited[x][y]:
            return 0
        visited[x][y] = True
        sides = 0
        sides += self.dfs(grid, x - 1, y, visited)
        sides += self.dfs(grid, x + 1, y, visited)
        sides += self.dfs(grid, x, y - 1, visited)
        sides += self.dfs(grid, x, y + 1, visited)
        return sides