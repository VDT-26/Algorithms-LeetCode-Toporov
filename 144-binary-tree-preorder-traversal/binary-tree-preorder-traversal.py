class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        answer = []                          
        def search(node):                    
            if not node:                  
                return                    
            answer.append(node.val)          
            search(node.left)                
            search(node.right)               
        search(root)                         
        return answer                        