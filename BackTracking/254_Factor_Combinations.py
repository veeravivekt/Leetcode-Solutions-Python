class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        return self.dfs(n, 2, [], [])
    
    def dfs(self, n, start, curr, result):
        for i in range(start, int(n ** 0.5) + 1):
            if n % i == 0:
                curr.append(i)
                print(curr)
                result.append(curr + [n // i])
                print(result)
                self.dfs(n // i, i, curr, result)
                curr.pop()
        return result