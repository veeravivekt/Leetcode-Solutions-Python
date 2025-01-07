# Brute Force
# EC: casesensitive?, contiguous?, only alpha?, repeated or unique?, max size of each word?, max arr size
class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        """
        ["mass","as","hero","superhero"]
        mass -> NONE
        as -> "mass"
        hero -> "superhero"
        superhero -> NONE
        result = ["as", "hero]
        """
        result = []
        for wordIndex in range(len(words)):
            for verifyIndex in range(len(words)):
                if wordIndex == verifyIndex:
                    continue
                if words[wordIndex] in words[verifyIndex]:
                    result.append(words[wordIndex])
                    break
        return result
# TC: O(m * n^2) = two nested loops * String match verification
# SC: O(m * n) = result array(max size is n) * length of longest array(m)