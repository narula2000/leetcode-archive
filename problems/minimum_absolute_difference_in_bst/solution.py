# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        lst = []
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            lst.append(node.val)
            inorder(node.right) 

        inorder(root) 

        diff = 1e10
        for i in range(1, len(lst)):
            diff = min(diff, lst[i] - lst[i-1])
        
        return diff