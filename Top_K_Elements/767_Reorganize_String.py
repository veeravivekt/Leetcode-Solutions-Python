class Solution:
    def reorganizeString(self, s: str) -> str:
        count = {}
        for c in s:
            count[c] = count.get(c, 0) + 1
        maxHeap = []
        for key, value in count.items():
            heappush(maxHeap, (-value, key))
        
        prevKey, prevValue = None, 0
        result = ""
        while maxHeap:
            value, key = heappop(maxHeap)
            if prevKey and -prevValue > 0:
                heappush(maxHeap, (prevValue, prevKey))
            result += key
            prevValue = value + 1
            prevKey = key
        return result if len(s) == len(result) else ""