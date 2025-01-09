class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        result = 0
        for word in words:
            if word.startswith(pref):
                result += 1
        return result
# TC: O(n * k) = checking each word O(n) * check if word has prefix O(k) where k is len of prefix
# SC: O(1)