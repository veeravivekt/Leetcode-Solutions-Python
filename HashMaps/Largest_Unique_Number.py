from collections import defaultdict

class Solution:
    def largestUniqueNumber(self, A: List[int]) -> int:
        maxUnique = -1
        # ToDo: Write Your Code Here.
        hashmap = {}
        for n in A:
            hashmap[n] = hashmap.get(n, 0) + 1
        for n in A:
            if hashmap[n] == 1:
                maxUnique = max(maxUnique, n)
        return maxUnique
