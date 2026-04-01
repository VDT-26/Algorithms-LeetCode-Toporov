# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root):
        def validate(node, low, high):
            if not node:
                return True #Базовый случай

            val = node.val #просто сохраняем в локальную переменную
 
            if (low is not None and val <= low) or \
               (high is not None and val >= high):
                return False

            return validate(node.left, low, val) and \
                   validate(node.right, val, high) #Рекурсивный спуск в поддеревья

        return validate(root, None, None)