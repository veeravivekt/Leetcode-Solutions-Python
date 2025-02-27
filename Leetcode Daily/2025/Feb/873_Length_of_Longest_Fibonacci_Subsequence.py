class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        """
        [1,2,3,4,5,6,7,8]
        1 + 2 = 3 + 2 = 5 + 3 = 8
        """
        numSet = set(arr)
        arrLen = len(arr)
        longestSeq = 0
        for i in range(arrLen):
            for j in range(i + 1, arrLen):
                prev = arr[j]
                curr = arr[i] + arr[j]
                currLen = 2
                
                while curr in numSet:
                    prev, curr = curr, curr + prev
                    currLen += 1
                    longestSeq = max(longestSeq, currLen)
        return longestSeq