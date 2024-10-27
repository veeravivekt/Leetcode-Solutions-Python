class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {')':'(', '}':'{', ']':'['}
        for b in s:
            if b in brackets:
                if not stack or brackets[b] != stack.pop():
                    return False
            else:
                stack.append(b)
        return not stack
                
