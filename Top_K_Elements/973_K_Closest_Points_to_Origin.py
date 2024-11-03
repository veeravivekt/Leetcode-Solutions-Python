class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        for i, x in enumerate(points):
            heappush(minHeap, ((x[0] ** 2 + x[1] ** 2) ** 0.5, points[i]))
        closest = []
        while k > 0:
            closest.append(heappop(minHeap)[1])
            k -= 1
        return closest
        