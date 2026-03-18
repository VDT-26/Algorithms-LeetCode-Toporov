from typing import List
import math
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = {"+", "-", "*", "/"}
        for token in tokens:
            if token not in ops:
                stack.append(int(token))
            else:
                b = stack.pop()
                a = stack.pop()
                if token == "+":
                    stack.append(a + b)
                elif token == "-":
                    stack.append(a - b)
                elif token == "*":
                    stack.append(a * b)
                else:  # division, truncate toward zero
                    # use int(a / b) to truncate toward zero
                    stack.append(int(a / b))
        return stack[-1]