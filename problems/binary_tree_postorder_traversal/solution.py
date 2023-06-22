# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        lst = []
        def helper(node):
            if not node:
                return
            
            helper(node.left)
            helper(node.right)
            lst.append(node.val)
        
        helper(root)
        
        return lst
            
