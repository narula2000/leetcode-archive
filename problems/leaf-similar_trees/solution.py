# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    lst = []
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        self.lst = []
        self.helper(root1)
        left = self.lst
        self.lst = []
        self.helper(root2)
        right = self.lst
        return left == right

    def helper(self, node):
        if not node:
            return

        if not node.left and not node.right:
            self.lst.append(node.val)
            return
        
        self.helper(node.left)
        self.helper(node.right)