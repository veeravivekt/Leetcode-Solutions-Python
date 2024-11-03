from heapq import *

class Solution:
  def minimumCostToConnectRopes(self, ropeLengths):
    minHeap = []
    for n in ropeLengths:
      heappush(minHeap, n)
    print(minHeap)
    cost = 0
    while len(minHeap) > 1:
      temp = heappop(minHeap) + heappop(minHeap)
      cost += temp
      heappush(minHeap, temp)
    return cost
