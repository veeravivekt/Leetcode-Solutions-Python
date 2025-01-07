# Brute Force
# EC: all 0's?, max size of boxes arr?, only 0's & 1's?, 
class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        """
        boxes = "110"
        1st box = 110 -> 200 (1 move)
        2nd box = 110 -> 020 (1 move)
        3rd box = 110 -> 101 -> 011 -> 002 (3 moves)
        result = [1, 1, 3]
        """
        result = [0] * len(boxes)
        for currBox in range(len(boxes)):
            if boxes[currBox] == '1':
                for newPosition in range(len(boxes)):
                    result[newPosition] += abs(newPosition - currBox)
        return result
# TC: O(n ** 2) = two nested loops iterating through every box
# SC: O(n) = result array

# Prefix Sum
class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        """
        110
        Left Pass:
        range (1, n)
        leftCount = 0 1 2
        leftCost  = 0 1 3
        result    = 0 1 3

        Right Pass:
        range(n - 2, -1, -1)
        rightCount = 1 0 0
        rightCost  = 1 0 0
        result     = 1 1 3
        """
        n = len(boxes)
        result = [0] * n
        leftCount, leftCost, rightCount, rightCost = 0, 0, 0, 0
        for i in range(1, n):
            if boxes[i - 1] == '1':
                leftCount += 1
            leftCost += leftCount
            result[i] = leftCost
        for i in range(n - 2, -1, -1):
            if boxes[i + 1] == '1':
                rightCount += 1
            rightCost += rightCount
            result[i] += rightCost
        return result
# TC: O(n) -> Left Pass O(n) + Right Pass O(n)
# SC: O(n) -> result O(n) + other variables O(1)