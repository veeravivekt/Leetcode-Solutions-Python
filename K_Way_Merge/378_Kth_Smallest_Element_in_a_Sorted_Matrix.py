class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        minHeap = []
        for i in range(len(matrix)):
            heappush(minHeap, (matrix[i][0], 0, matrix[i]))
        count, n = 0, 0
        while minHeap:
            n, i, row = heappop(minHeap)
            count += 1
            if count == k:
                break
            if len(matrix) > i + 1:
                heappush(minHeap, (row[i + 1], i + 1, row))
        return n