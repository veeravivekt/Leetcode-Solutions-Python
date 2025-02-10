#EC: more digits and less alpha?, more alpha less digits?, max digits?, only alphanum?, what if no left chars?
class Solution:
    def clearDigits(self, s: str) -> str:
        """
        bc44b3cs24
        stack = b->bc->b-> ->b-> ->c->cs->c-> (end)
        cb34
        stack = c -> cb -> "c" remove b -> "" remove c(end)
        """
        alpha_stack = []
        for c in s:
            if c.isalpha():
                alpha_stack.append(c)
            else:
                alpha_stack.pop()
        return "".join(alpha_stack)
# TC: O(n) -> iterating every single char only once, append and pop(O(1))
# SC: O(n) -> alpha_stack can store maximum of n chars where all chars are alphabets