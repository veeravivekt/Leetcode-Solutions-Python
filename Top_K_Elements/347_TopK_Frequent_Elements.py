class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            count[n] = count.get(n, 0) + 1
        
        maxHeap = []
        for key, value in count.items():
            heappush(maxHeap, (-value, key))
        
        topK = []
        for _ in range(k):
            value, key = heappop(maxHeap)
            topK.append(key)
        return topK