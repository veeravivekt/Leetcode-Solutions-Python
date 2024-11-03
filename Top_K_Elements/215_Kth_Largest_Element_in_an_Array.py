class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxHeap = []
        for n in nums:
            heappush(maxHeap, -n)
        while k > 1:
            heappop(maxHeap)
            k -= 1
        return -maxHeap[0]