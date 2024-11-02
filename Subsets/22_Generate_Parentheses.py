class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        result = []
        def generation(stack, openN, closeN):
            if openN == closeN == n:
                result.append("".join(stack))
                return
            if openN < n:
                stack.append('(')
                generation(stack, openN + 1, closeN)
                stack.pop()
            if closeN < openN:
                stack.append(')')
                generation(stack, openN, closeN + 1)
                stack.pop()
        generation(stack, 0, 0)
        return result