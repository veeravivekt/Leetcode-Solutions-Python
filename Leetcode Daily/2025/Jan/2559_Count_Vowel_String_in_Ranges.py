# EC: alpha only?, size of each word?, size of word arr?, query arr size?, each query size?, case sensitive?
class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        """
        words = ["aba","bcb","ece","aa","e"]
        queries = [[0,2],[1,4],[1,1]]
        startEndVowels = [1, 0, 1, 1, 1]
                         [0, 1, 2, 3, 4]
        result = [2, 3, 0]
        """
        vowels = {'a', 'e', 'i', 'o', 'u'}
        prefix = [0] * (len(words) + 1)
        for i, w in enumerate(words):
            prefix[i + 1] = prefix[i]
            if w[0] in vowels and w[-1] in vowels:
                prefix[i + 1] += 1
        
        result = []
        for q in queries:
            result.append(prefix[q[1] + 1] - prefix[q[0]])
        return result
# TC: O(n + m) = prefix calculation O(n) + query processing O(m) (n is no of words, m is queries)
# SC: O(n + m) = prefix array O(n) + result array O(m) + set O(5)