class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        i = 0
        while i < len(arr):
            j = arr[i] - 1
            if arr[i] > 0 and arr[i] <= len(arr) and arr[i] != arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
            else:
                i += 1
        
        extraNumbers = []
        missingNumber = 0
        i = 0
        while i < len(arr) and k > 0:
            missingNumber = i + 1
            if i + 1 != arr[i]:
                extraNumbers.append(arr[i])
                k -= 1
            i += 1
        
        while k > 0:
            missingNumber += 1
            if missingNumber not in extraNumbers:
                k -= 1
        return missingNumber
