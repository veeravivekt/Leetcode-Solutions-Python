class Solution:
  def findMaxSumSubArray(self,k, arr):
    # TODO: Write your code here
    maxSum = -math.inf
    left = 0
    sum = 0
    for right in range(len(arr)):
        sum += arr[right]
        if right - left + 1 >= k:
            maxSum = max(maxSum, sum)
            sum -= arr[left]
            left += 1
    return maxSum

    
