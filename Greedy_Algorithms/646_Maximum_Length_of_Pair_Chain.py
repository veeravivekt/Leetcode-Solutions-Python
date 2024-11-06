class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key = lambda x: x[1])
        end = -math.inf
        length = 0

        for pair in pairs:
            if pair[0] > end:
                end = pair[1]
                length += 1
        return length