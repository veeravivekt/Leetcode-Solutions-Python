class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        start, end = 0, math.inf
        currMax = -math.inf
        minHeap = []
        for arr in nums:
            heappush(minHeap, (arr[0], 0, arr))
            currMax = max(currMax, arr[0])
        while len(minHeap) == len(nums):
            num, i, arr = heappop(minHeap)
            if end - start > currMax - num:
                start, end = num, currMax
            if len(arr) > i + 1:
                heappush(minHeap, (arr[i + 1], i + 1, arr))
                currMax = max(currMax, arr[i + 1])
        return [start, end]