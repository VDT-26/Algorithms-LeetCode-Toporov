class MyCircularQueue:
    def __init__(self, k: int):
        # Ёмкость буфера
        self.k = k
        # Массив фиксированного размера k
        self.buf = [0] * k
        # Индекс головы (элемент для Front)
        self.head = 0
        # Индекс следующей позиции для вставки (tail указывает на место вставки)
        self.tail = 0
        # Текущее число элементов
        self.count = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.buf[self.tail] = value
        # сдвигаем tail по модулю k
        self.tail = (self.tail + 1) % self.k
        self.count += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        # просто сдвигаем head по модулю k — старое значение считается удалённым
        self.head = (self.head + 1) % self.k
        self.count -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.buf[self.head]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        # последний элемент находится на позиции (tail - 1 + k) % k
        return self.buf[(self.tail - 1 + self.k) % self.k]

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == self.k   


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()