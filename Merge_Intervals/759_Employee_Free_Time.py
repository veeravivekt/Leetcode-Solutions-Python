"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        sSorted = sorted([i for s in schedule for i in s], key = lambda x: x.start)
        freeTime = []
        prev = sSorted[0]
        for interval in sSorted[1:]:
            if prev.end >= interval.start and prev.end < interval.end:
                prev.end = interval.end
            elif prev.end < interval.start:
                freeTime.append(Interval(prev.end, interval.start))
                prev = interval
        return freeTime