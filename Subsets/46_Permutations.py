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
    