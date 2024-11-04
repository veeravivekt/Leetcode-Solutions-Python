class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        count = {}
        for n in arr:
            count[n] = count.get(n, 0) + 1
        minHeap = []
        for key, value in count.items():
            heappush(minHeap, (value, key))
        while k > 0:
            value, key = heappop(minHeap)
            while value > 0 and k > 0:
                count[key] -= 1
                k -= 1
                if count[key] == 0:
                    del count[key]
                    break
        return len(count.keys())
            
