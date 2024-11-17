class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()
        def backtrack(target, start, combo):
            if target == 0:
                result.append(list(combo))
                return
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                if candidates[i] > target:
                    break
                combo.append(candidates[i])
                backtrack(target - candidates[i], i + 1, combo)
                combo.pop()
        backtrack(target, 0, [])
        return result