class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        strings = [""]
        for c in s:
            for _ in range(len(strings)):
                s = strings.pop(0)
                if c.isalpha():
                    strings.extend([s + c.lower(), s + c.upper()])
                else:
                    strings.append(s + c)
        return strings