class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        """
        1 + 8 = 9 : 0
        4 + 3 = 7 : 1
        3 + 6 = 9 : 2
        1 + 3 = 4 : 3
        7     = 7 : 4
        """
        digit_sum_pairs = []
        # calculate digits sums for each index
        for i, n in enumerate(nums):
            sum_of_digits = 0
            while n > 0:
                sum_of_digits += n % 10
                n //= 10
            digit_sum_pairs.append((sum_of_digits, nums[i]))
        
         
        digit_sum_pairs.sort() # sort to get all same sums beside each other

        # check if sum of digits have pairs and calculate their max sum of pairs
        result = -1
        for i in range(1, len(digit_sum_pairs)):
            curr_sum = digit_sum_pairs[i][0]
            prev_sum = digit_sum_pairs[i - 1][0]
            if curr_sum == prev_sum:
                result = max(result, digit_sum_pairs[i][1] + digit_sum_pairs[i - 1][1])
        return result
# TC: O(n log n) -> each number is being iterated O(n) + sorting O(n log n) + each sum pair is being iterated O(n)
# SC: O(n) -> array for storing n sum of digits O(n)