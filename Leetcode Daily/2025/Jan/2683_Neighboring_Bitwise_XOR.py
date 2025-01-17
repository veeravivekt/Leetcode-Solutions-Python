class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        return self.validation(derived, [0]) or self.validation(derived, [1])

    def validation(self, derived, original):
        for i in range(len(derived)):
            original.append(derived[i] ^ original[i])
        return original[0] == original[-1]
# TC: O(n) = iterates derived array twice O(n) + O(n)
# SC: O(n) = original array (same size as derived array) O(n)