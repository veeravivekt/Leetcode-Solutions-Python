# Subsets TC: O(n! * n) SC: O(n! * n)
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = [[]]
        for n in nums:
            for _ in range(len(permutations)):
                p = permutations.pop(0)
                for i in range(len(p) + 1):
                    currentP = list(p)
                    currentP.insert(i, n)
                    permutations.append(currentP)
        return permutations

# BackTracking TC: O(n! * n^2) SC: O(n! * n)
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]
        result = []
        perms = self.permute(nums[1:])
        for p in perms:
            for i in range(len(p) + 1):
                currP = p.copy()
                currP.insert(i, nums[0])
                result.append(currP)
        return result