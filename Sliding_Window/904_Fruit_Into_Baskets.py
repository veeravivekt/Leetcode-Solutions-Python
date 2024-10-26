class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        baskets = {}
        left = 0
        fruitsMax = -math.inf
        for right in range(len(fruits)):
            baskets[fruits[right]] = baskets.get(fruits[right], 0) + 1
            while len(baskets) > 2:
                baskets[fruits[left]] -= 1
                if baskets[fruits[left]] == 0: baskets.pop(fruits[left])
                left += 1
            fruitsMax = max(fruitsMax, right - left + 1)
        return fruitsMax