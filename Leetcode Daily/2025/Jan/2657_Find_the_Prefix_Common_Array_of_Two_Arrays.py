class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        """
        A = [1,3,2,4]
        B = [3,1,2,4]
        [0 , 2(1, 3), 3(1, 2, 3), 4(1, 2, 3, 4)]
        """
        result = [0] * len(A)
        setA = set()
        for i in range(len(A)):
            setA.add(A[i])
            count = 0
            for j in range(i + 1):
                if B[j] in setA:
                    count += 1
            result[i] = count
        return result
# TC: O(n ^ 2) = nested loops
# SC: O(n) = result array O(n), set O(n), both can store max of n nums