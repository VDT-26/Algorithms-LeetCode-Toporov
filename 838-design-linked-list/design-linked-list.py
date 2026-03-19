class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class MyLinkedList:
    def __init__(self):
        self.head = Node(0)  # фиктивный (dummy) узел
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size: # проверяем индекс
            return -1
        curr = self.head.next 
        for _ in range(index):
            curr = curr.next
        return curr.val

    def addAtHead(self, val: int) -> None: # Вставка в индекс 0
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None: # Вставка в конец
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None: # Добавить в индекс
        if index < 0:
            index = 0
        if index > self.size:
            return
# перенастройка связей
        prev = self.head
        for _ in range(index):
            prev = prev.next

        node = Node(val)
        node.next = prev.next
        prev.next = node
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return

        prev = self.head
        for _ in range(index):
            prev = prev.next

        prev.next = prev.next.next
        self.size -= 1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)