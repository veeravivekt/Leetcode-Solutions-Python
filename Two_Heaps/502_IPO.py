class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        minCapital = []
        maxProfit = []
        funds = w
        for i, c in enumerate(capital):
            heappush(minCapital, (c, i))
        
        for _ in range(k):
            while minCapital and minCapital[0][0] <= funds:
                c, i = heappop(minCapital)
                heappush(maxProfit, -profits[i])
            if not maxProfit:
                break
            funds += -heappop(maxProfit)
        return funds