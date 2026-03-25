class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        answer = []
        def search(node): 
            if not node: # Если пусто -- выходим
                return 0
            search(node.left)   # Идем влево
            answer.append(node.val) # Добавляем значение в ответный список
            search(node.right)  # Идём вправо
        search(root)    # Идём наверх
        return answer