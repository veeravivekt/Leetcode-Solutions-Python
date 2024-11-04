class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        minHeap = []
        for n in arr:
            heappush(minHeap, (abs(n - x), n))
        kClosest = []
        for _ in range(k):
            diff, value = heappop(minHeap)
            kClosest.append(value)
        kClosest.sort()
        return kClosest