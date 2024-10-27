class Solution:
  def findNumbers(self, nums):
    duplicateNumbers = []
    # TODO: Write your code here
    i, n = 0, len(nums)
    while i < n:
      j = nums[i] - 1
      if nums[i] != nums[j]:
        nums[i], nums[j] = nums[j], nums[i]
      else:
        i += 1
    for i in range(n):
      if i + 1 != nums[i]:
        duplicateNumbers.append(nums[i])
    
    return duplicateNumbers
