# Normal Method
class Solution:
    def isHappy(self, n: int) -> bool:
        hashset = set()
        while n != 1:
            sum = 0
            while n > 0:
                sum += (n % 10) ** 2
                n = n // 10
            if sum in hashset:
                return False
            else:
                n = sum
                hashset.add(n)
        return True
    
# Fast and Slow Pointer 
class Solution:
    def isHappy(self, n: int) -> bool:
        slow, fast = n, n
        while True:
            slow = self.squareSum(slow)
            fast = self.squareSum(self.squareSum(fast))
            if slow == fast:
                break
        return slow == 1
    
    def squareSum(self, n):
        sum = 0
        while n > 0:
            sum += (n % 10) ** 2
            n //= 10
        return sum