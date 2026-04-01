class Solution:
    def deleteNode(self, root, key):
        if not root:
            return None

        # Ищем узел
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            # Случай 1: нет детей
            if not root.left and not root.right:
                return None

            # Случай 2: один ребёнок
            if not root.left:
                return root.right
            if not root.right:
                return root.left

            # Случай 3: два ребёнка
            # Находим минимальный узел справа
            successor = root.right
            while successor.left:
                successor = successor.left

            # Копируем значение
            root.val = successor.val

            # Удаляем successor из правого поддерева
            root.right = self.deleteNode(root.right, successor.val)

        return root