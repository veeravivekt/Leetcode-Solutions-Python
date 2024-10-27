class Solution:
    def reverseString(self, s):
       # ToDo: Write Your Code Here.
        stack = []
        for c in s:
            stack.append(c)
        s = ""
        while stack:
            s += stack.pop()
        return s


