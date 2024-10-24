class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        first, second = -1, -1
        answer = len(wordsDict)
        for i, word in enumerate(wordsDict):
            if word == word1:
                first = i
            if word == word2:
                second = i
            if first != -1 and second != -1:
                answer = min(answer, abs(first - second))
        return answer