from heapq import *

class Solution:
  def findKthSmallestNumber(self, nums, k):
    minheap = []
    for n in nums:
      heappush(minheap, n)
    while k > 1:
      heappop(minheap)
      k -= 1
    return minheap[0]
