# Top Down approach
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        dp = [[-1] * 2 for _ in range(len(nums))]
        def dfs(i, flag):
            if i >= len(nums) or (flag and i == len(nums) - 1):
                return 0
            if dp[i][flag] != -1:
                return dp[i][flag]
            dp[i][flag] = max(dfs(i + 1, flag), nums[i] + dfs(i + 2, flag))
            return dp[i][flag]
        return max(dfs(0, True), dfs(1, False))

# Bottom Up Approach
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def dfs(nums):
            if not nums:
                return 0
            if len(nums) == 1:
                return nums[0]
            dp = [0] * len(nums)
            dp[0] = nums[0]
            dp[1] = max(nums[0], nums[1])
            for i in range(2, len(nums)):
                dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])
            return dp[-1]
        return max(dfs(nums[1:]), dfs(nums[:-1]))