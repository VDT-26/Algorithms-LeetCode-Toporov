class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        answer = []
        def search(node):
            if not node:
                return
            search(node.left) # Влево до конца
            search(node.right) # 
            answer.append(node.val)
        search(root)
        return answer