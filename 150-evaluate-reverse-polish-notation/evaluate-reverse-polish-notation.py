class Solution:
    def evalRPN(self, tokens):
        """
        tokens: список, в котором могут быть как числа, так и операторы.
        """
        stack = []
        for token in tokens: # Если число -- добавляем в стэк, если нет -- убираем последние два значения и выполняем операцию.
            if token == "+": 
                b = stack.pop()
                a = stack.pop()
                stack.append(a + b)
            elif token == "-":
                b = stack.pop()
                a = stack.pop()
                stack.append(a - b)
            elif token == "*":
                b = stack.pop()
                a = stack.pop()
                stack.append(a * b)
            elif token == "/":
                b = stack.pop()
                a = stack.pop()
                # Деление должно усекаться к нулю
                stack.append(int(a / b))
            else:
                # токен — число (возможно со знаком)
                stack.append(int(token))
        return stack[-1] if stack else 0