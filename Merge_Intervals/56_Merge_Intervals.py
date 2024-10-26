class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        mergedIntervals = []
        intervals.sort(key = lambda x: x[0])
        start = intervals[0]
        for interval in intervals[1:]:
            if start[1] >= interval[0]:
                start[1] = max(start[1], interval[1])
            else:
                mergedIntervals.append(start)
                start = interval
        mergedIntervals.append(start)
        return mergedIntervals