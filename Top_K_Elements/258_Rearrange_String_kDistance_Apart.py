class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        if k <= 1:
            return s
        count = {}
        for c in s:
            count[c] = count.get(c, 0) + 1
        maxHeap = []
        for key, value in count.items():
            heappush(maxHeap, (-value, key))
        queue = []
        result = ""
        while maxHeap:
            value, key = heappop(maxHeap)
            result += key
            queue.append((key, value + 1))
            if len(queue) == k:
                k1, v1 = queue.pop(0)
                if -v1 > 0:
                    heappush(maxHeap, (v1, k1))  
        return result if len(result) == len(s) else ""