class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        result = []
        if "+" not in expression and "-" not in expression and "*" not in expression:
            result.append(int(expression))
        else:
            for i in range(len(expression)):
                c = expression[i]
                if not c.isdigit():
                    left = self.diffWaysToCompute(expression[0:i])
                    right = self.diffWaysToCompute(expression[i + 1 :])
                    for l in left:
                        for r in right:
                            if c == '+':
                                result.append(l + r)
                            elif c == '-':
                                result.append(l - r)
                            elif c == '*':
                                result.append(l * r)
        return result