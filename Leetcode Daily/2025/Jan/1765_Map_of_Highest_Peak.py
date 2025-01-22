class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        """
        isWater = [[0,1],[0,0]]
        0 = land, 1 = water
        """
        rows = len(isWater)
        cols = len(isWater[0])
        # intialize heights with -1 as defult value
        heights = [[-1 for _ in range(cols)] for _ in range(rows)]
        # add all values from isWater to queue and set thier height to 0
        cell_queue = deque()
        for r in range(rows):
            for c in range(cols):
                if isWater[r][c] == 1:
                    heights[r][c] = 0
                    cell_queue.append((r, c))
        # direction movement helper arrays (N, E, S, W)
        dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
        """
        00 01 02
        10 11 12
        20 21 22
        """
        layer_height = 1
        # BFS all cells in matrix
        while cell_queue:
            # check every element in queue
            length_of_queue = len(cell_queue)
            for _ in range(length_of_queue):
                curr_cell = cell_queue.popleft()
                # check all 4 directions
                for i in range(4):
                    adj_x = curr_cell[0] + dx[i]
                    adj_y = curr_cell[1] + dy[i]
                    # check if cell is unprocessed and valid(not out of bounds)
                    if self.validCell(adj_x, adj_y, rows, cols) and heights[adj_x][adj_y] == -1:
                        cell_queue.append((adj_x, adj_y))
                        # assign height to cell based on layer
                        heights[adj_x][adj_y] = layer_height
            # increment layer
            layer_height += 1
        return heights
    
    # helper func
    def validCell(self, x, y, rows, cols):
        return 0 <= x < rows and 0 <= y < cols
    
# O(m * n) Where m is the number of rows and n is the number of columns in the input matrix. The algorithm visits each cell exactly once.
# O(m * n) The space is used for the heights matrix and the cell_queue. In the worst case, the queue might contain all cells of the matrix.