# EC: Can word1 or word2 be null?, can wordDict be empty?, Max Lenth of words?, Max Length of wordDict?, word1 == word2?, casesensitive?, word1, word2 always exists in wordDict? multiple occurances?
"""
word1 = "coding", word2 = "practice"
["practice", "makes", "perfect", "coding", "makes"]
s0: p1 = -1 | p2 = -1
s1: p1 = -1 | p2 = 0
s2: p1 = 3 | p2 = 0 | result = 3 - 0
"""
class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        # initialize a shortDist variable to keep track
        shortDist = math.inf
        # initalize two variables called position1 and postion 2 with -1
        position1, position2 = -1, -1
        # check each element in wordsDict to find word1 or word2
        for i, word in enumerate(wordsDict):
            if word == word1:
                position1 = i
            if word == word2:
                position2 = i
            # word1 and word2 found then update shortDist variable
            if position1 != -1 and position2 != -1:
                shortDist = min(shortDist, abs(position1 - position2))
        return shortDist
# TC: O(n) -> checking each word at most once
# SC: O(1) -> shortDist, position1, position2 (O(1))