class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        maxStartHeap = []
        maxEndHeap = []
        result = [-1 for i in range(len(intervals))]
        for i in range(len(intervals)):
            heappush(maxStartHeap, (-intervals[i][0], i))
            heappush(maxEndHeap, (-intervals[i][1], i))
        
        for _ in range(len(intervals)):
            end, j = heappop(maxEndHeap)
            if -maxStartHeap[0][0] >= -end:
                start, i = heappop(maxStartHeap)
                while maxStartHeap and -maxStartHeap[0][0] >= -end:
                    start, i = heappop(maxStartHeap)
                result[j] = i
                heappush(maxStartHeap, (start, i))
        return result