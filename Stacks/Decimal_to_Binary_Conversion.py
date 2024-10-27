class Solution: 
    def decimalToBinary(self, num):
        # ToDo: Write Your Code Here.
        stack = []
        while num > 0:
            stack.append(num % 2)
            num //= 2
        binary = ''
        while stack:
            binary += str(stack.pop())
        return binary
