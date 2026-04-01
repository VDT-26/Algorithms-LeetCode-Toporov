class Solution:
    def insertIntoBST(self, root, val):
        # Если дерево пустое — новый узел становится корнем
        if not root:
            return TreeNode(val)

        # Если вставляемое значение меньше — идём влево
        if val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        else:
            # Иначе — вправо (по условию val уникален)
            root.right = self.insertIntoBST(root.right, val)

        return root