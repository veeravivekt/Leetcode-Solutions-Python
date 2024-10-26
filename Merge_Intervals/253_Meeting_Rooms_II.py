class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        minHeap = []
        minRoom = 0
        intervals.sort(key = lambda x: x[0])
        for interval in intervals:
            while minHeap and interval[0] >= minHeap[0]:
                heapq.heappop(minHeap)
            heapq.heappush(minHeap, interval[1])
            minRoom = max(minRoom, len(minHeap))
        return minRoom