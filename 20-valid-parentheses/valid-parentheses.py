class Solution:
    def isValid(self, s: str) -> bool:
        # Словарь соответствий закрывающих → открывающих скобок
        pairs = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        stack = []
        for ch in s:
            # Если открывающая скобка — кладём в стек
            if ch in '([{':
                stack.append(ch)
            else:
                # Если стек пуст — закрывать нечего
                if not stack:
                    return False
                # Снимаем верхнюю скобку
                top = stack.pop()
                # Проверяем соответствие
                if top != pairs[ch]:
                    return False
        # Если стек пуст — всё корректно
        return len(stack) == 0