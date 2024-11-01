class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        distinctIslands = set()
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    distinctIslands.add(self.dfs(grid, i, j, '0'))
        print(distinctIslands)
        return len(distinctIslands)
    
    def dfs(self, grid, x, y, island):
        if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
            return ''
        if grid[x][y] == 0:
            return ''
        grid[x][y] = 0
        currentIsland = island
        currentIsland += self.dfs(grid, x - 1, y, 'U')
        currentIsland += self.dfs(grid, x + 1, y, 'D')
        currentIsland += self.dfs(grid, x, y - 1, 'L')
        currentIsland += self.dfs(grid, x, y + 1, 'R')
        currentIsland += 'B'
        return currentIsland
        