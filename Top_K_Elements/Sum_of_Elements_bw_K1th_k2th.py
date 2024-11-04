from heapq import *

class Solution:
  def findSumOfElements(self, nums, k1, k2):
    elementSum = 0
    # TODO: Write your code here
    minHeap = []
    for n in nums:
      heappush(minHeap, n)
    for _ in range(k1):
      heappop(minHeap)
    for _ in range(k2 - k1 - 1):
      elementSum += heappop(minHeap)
    return elementSum
