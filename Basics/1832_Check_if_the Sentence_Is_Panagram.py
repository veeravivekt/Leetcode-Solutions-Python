class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alpha = [0] * 26
        for s in sentence:
            alpha[ord(s) - ord('a')] += 1
        for i in range(26):
            if alpha[i] < 1:
                return False
        return True