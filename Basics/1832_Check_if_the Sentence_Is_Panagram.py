# Approach: Array
# EC: casesenstive?, maxsize of sentence?, empty string
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        # initalize a arr to store count of chars
        charStore = [0] * 26
        # iterate through every single character in string
        for c in sentence:
            # add count to charstore
            charStore[ord(c) - ord('a')] += 1
        # verify if every alphabet is repated atleast once and return result
        for n in charStore:
            if n == 0:
                return False
        return True

# TC: O(n) -> each char is iterated atmost once(O(n)) + charStore verify(O(26) = O(1))
# SC: O(1) -> charStore(O(26) = O(1))