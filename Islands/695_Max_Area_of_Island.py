class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        maxArea = 0

        for i in range(rows):
            for j in range(cols):
                maxArea = max(maxArea, self.dfs(grid, i, j))
        return maxArea
    def dfs(self, grid, x, y):
        if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
            return 0
        if grid[x][y] == 0:
            return 0
        grid[x][y] = 0
        area = 1
        area += self.dfs(grid, x - 1, y)
        area += self.dfs(grid, x + 1, y)
        area += self.dfs(grid, x, y - 1)
        area += self.dfs(grid, x, y + 1)
        return area