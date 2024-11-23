# Approach: Two Pointers
# TC: O(n) -> Each char is checked at most once
# SC: O(n) -> charStore(O(10) -> O(1)), arr(O(n)), left, right(O(1))
class Solution:
    def reverseVowels(self, s: str) -> str:
        # convert all the vowels into a set 
        charStore = set("AEIOUaeiou")
        # initialize pointers for start and end of the string
        left, right = 0, len(s) - 1
        arr = list(s)
        while left < right:
            # increment the left pointer until a vowel is found
            while left < right and arr[left] not in charStore:
                left += 1
            # decrement the right pointer until a vowel is found
            while left < right and arr[right] not in charStore:
                right -= 1
            # swap the values of left and right if both are vowels
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
        return "".join(arr)