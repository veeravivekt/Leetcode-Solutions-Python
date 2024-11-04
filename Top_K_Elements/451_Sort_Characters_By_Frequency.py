class Solution:
    def frequencySort(self, s: str) -> str:
        count = {}
        for c in s:
            count[c] = count.get(c, 0) + 1
        
        maxHeap = []
        for key, value in count.items():
            heappush(maxHeap, (-value, key))
        sortedStr = ""
        while maxHeap:
            value, key = heappop(maxHeap)
            sortedStr += (key * (-value))
        return sortedStr
