class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        answer = []
        def search(node): 
            if not node: # Если пусто -- выходим
                return 0
            search(node.left)   # Идем влево до последнего
            answer.append(node.val) # Левое поддерево уже обработано -- можно записать значение текущего узла
            search(node.right)  # Идём вправо до последнего
        search(root)    # Начинаем с корня
        return answer