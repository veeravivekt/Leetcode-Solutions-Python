class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for i in s:
            if stack and i == stack[-1][0]:
                char = stack.pop() + i
                stack.append(char)
            else:
                stack.append(i)
            if len(stack[-1]) == k:
                    stack.pop()
        return "".join(stack)
