# EC: casesensitive?, only alpha?, maxlen of string?, prefix and suffix have common chars?
class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        # check each index pairs
        result = 0
        for i in range(len(words) - 1):
            for j in range(i + 1, len(words)):
                if self.isPrefixAndSuffix(words[i], words[j]):
                    result += 1
        return result

    def isPrefixAndSuffix(self, str1, str2):
        return str2.startswith(str1) and str2.endswith(str1)
# TC: O(n^2 * m) = nested loops O(n^2) * check if prefix and suffix O(m) m is len of string
# SC: O(1)
