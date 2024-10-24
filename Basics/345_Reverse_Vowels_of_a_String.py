class Solution:
    vowels = "aeiouAEIOU"
    def reverseVowels(self, s: str) -> str:
        l, r = 0, len(s) - 1
        arr = list(s)
        while l < r:
            while l < r and self.vowels.find(arr[l]) == -1:
                l += 1
            while l < r and self.vowels.find(arr[r]) == -1:
                r -= 1
            arr[l], arr[r] = arr[r], arr[l]
            l += 1
            r -= 1
        return "".join(arr)