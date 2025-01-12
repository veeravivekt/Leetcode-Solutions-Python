class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        """
        s       = ") ) ( ) ) )"
                = "| ) | ) | |"
        locked  = "0 1 0 1 0 0"
        changed = "( ) ( ) ( )"
        """
        length = len(s)
        if length % 2 != 0:
            return False
        
        openStack = []
        unlockedStack = []
        for i in range(length):
            if locked[i] == "0":
                unlockedStack.append(i)
            elif s[i] == "(":
                openStack.append(i)
            elif s[i] == ")":
                if openStack:
                    openStack.pop()
                elif unlockedStack:
                    unlockedStack.pop()
                else:
                    return False
        while openStack and unlockedStack and openStack[-1] < unlockedStack[-1]:
            openStack.pop()
            unlockedStack.pop()
        
        if openStack:
            return False

        return True
# TC: O(n) = check open brackets and unlocked O(n) + matching O(n)
# SC: O(n) = openStack and unlockedStack
