class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        self.backtrack(candidates, target, 0, [], result)
        return result
    
    def backtrack(self, candidates, target, start, combo, result):
        if target == 0:
            result.append(list(combo))
            return
        
        for i in range(start, len(candidates)):
            if target < candidates[i]:
                continue
            combo.append(candidates[i])
            self.backtrack(candidates, target - candidates[i], i, combo, result)
            combo.pop()