class Solution:
  def findNumbers(self, nums):
    missingNumbers = []
    # TODO: Write your code here
    i = 0
    n = len(nums)
    while i < n:
      j = nums[i] - 1
      if j < n and nums[i] != nums[j]:
        nums[i], nums[j] = nums[j], nums[i]
      else:
        i += 1
    print(nums)
    for i in range(n):
      if i + 1 != nums[i]:
        missingNumbers.append(i + 1)
    return missingNumbers
