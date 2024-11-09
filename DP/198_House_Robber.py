# Top Down Approach
class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [-1] * len(nums)
        def dfs(i):
            if i >= len(nums):
                return 0
            if dp[i] != -1:
                return dp[i]
            dp[i] = max(dfs(i + 1), nums[i] + dfs(i + 2)) 
            return dp[i]
        return dfs(0)
    
# Bottom Up Approach
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(dp[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])
        return dp[-1]
        