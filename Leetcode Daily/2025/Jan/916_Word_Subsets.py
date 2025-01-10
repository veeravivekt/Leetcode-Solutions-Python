# EC: caseSensitive?, all words1 unique?, multiple same chars in words2?, max len?, words2 are single character or multiple?
class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        """
        charStore = [0] * 26
        wordStore = [0] * 26
        e = 1, o = 1
        a = 2, m = 1, z = 1, o = 1, n = 1
        """
        # helper function to count every character in strings
        def count(word):
            charStore = [0] * 26
            for c in word:
                charStore[ord(c) - ord('a')] += 1
            return charStore
        
        # count the max possible word2 occurances
        words2Store = [0] * 26
        for word2 in words2:
            for i, c in enumerate(count(word2)):
                words2Store[i] = max(words2Store[i], c)
        

        # verify which words1 match with words2 count
        result = []
        for word1 in words1:
            if all(x >= y for x, y in zip(count(word1), words2Store)):
                result.append(word1)
        return result
# TC: O(n * k1 + m * k2), Where: n = len(words1), m = len(words2), k1 = average length of words in words1, k2 = average length of words in words2
# SC: O(n) = fixed sized arrays O(26) + result can have max all words1 O(n)
