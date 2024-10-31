class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] != color:
            self.dfs(image, sr, sc, image[sr][sc], color)
        return image

    def dfs(self, image, x, y, oldColor, newColor):
            if x < 0 or x >= len(image) or y < 0 or y >= len(image[0]):
                return
            if image[x][y] != oldColor:
                return
            image[x][y] = newColor
            self.dfs(image, x - 1, y, oldColor, newColor)
            self.dfs(image, x + 1, y, oldColor, newColor)
            self.dfs(image, x, y - 1, oldColor, newColor)
            self.dfs(image, x, y + 1, oldColor, newColor)
