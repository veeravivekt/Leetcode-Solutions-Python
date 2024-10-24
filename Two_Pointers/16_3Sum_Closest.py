class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest = math.inf
        for i in range(len(nums) - 2):
            l, r = i + 1, len(nums) - 1
            while l < r:
                targetDiff = target - nums[i] - nums[l] - nums[r]
                if targetDiff == 0:
                    return target
                
                if abs(targetDiff) < abs(closest) or (abs(targetDiff) == abs(closest) and targetDiff > closest):
                    closest = targetDiff
                if targetDiff > 0:
                    l += 1
                else:
                    r -= 1
        return target - closest