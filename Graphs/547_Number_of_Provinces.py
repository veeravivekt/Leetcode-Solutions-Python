class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(city):
            for i in range(len(isConnected)):
                if isConnected[city][i] == 1 and not visited[i]:
                    visited[i] = True
                    dfs(i)

        province = 0
        visited = [False] * len(isConnected)
        for city in range(len(isConnected)):
            if not visited[city]:
                dfs(city)
                province += 1
        return province