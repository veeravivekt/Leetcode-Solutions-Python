class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
       """
       nums = ["111","011","001"]
       0                1
       00      01       10      11
       000 001 010 011  100 101 110 111
       """
       nums_set = set(nums)
       n = len(nums[0])
       missing = []
       self.findString(nums_set, "", missing, n)
       return missing[0]
    
    def findString(self, nums_set, currStr, missing, n):
        if currStr not in nums_set and len(currStr) == n:
            missing.append(currStr)
            return
        for b in ['0', '1']:
            if len(currStr) < n:
                self.findString(nums_set, currStr + b, missing, n)
# TC: O(2^n) - The function generates all possible binary strings of length n recursively.
# SC: O(n + len(nums)) - The recursion depth is n, and nums_set stores len(nums) elements