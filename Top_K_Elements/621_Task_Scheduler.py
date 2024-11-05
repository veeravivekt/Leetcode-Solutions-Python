class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = {}
        for t in tasks:
            count[t] = count.get(t, 0) + 1
        maxHeap = []
        for key, value in count.items():
            heappush(maxHeap, (-value, key))
        
        time = 0
        while maxHeap:
            queue = []
            interval = n + 1
            while interval > 0 and maxHeap:
                time += 1
                value, key = heappop(maxHeap)
                if -value > 1:
                    queue.append((value + 1, key))
                interval -= 1
            for value, key in queue:
                heappush(maxHeap, (value, key))
            if maxHeap:
                time += interval
        return time

            
