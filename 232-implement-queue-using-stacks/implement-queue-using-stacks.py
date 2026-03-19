class MyQueue:
    def __init__(self):
        # Стек для входящих элементов
        self.in_stack = []
        # Стек для исходящих элементов
        self.out_stack = []

    def push(self, x: int) -> None:
        # Всегда кладём в in_stack
        self.in_stack.append(x)

    def _move_in_to_out(self) -> None:
        # Переносим все элементы из in_stack в out_stack
        while self.in_stack:
            self.out_stack.append(self.in_stack.pop())

    def pop(self) -> int:
        # Если out_stack пуст, восстанавливаем порядок
        if not self.out_stack:
            self._move_in_to_out()
        return self.out_stack.pop()

    def peek(self) -> int:
        # Если out_stack пуст, восстанавливаем порядок
        if not self.out_stack:
            self._move_in_to_out()
        return self.out_stack[-1]

    def empty(self) -> bool:
        # Очередь пуста тогда и только тогда, когда оба стека пусты
        return not self.in_stack and not self.out_stack

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()