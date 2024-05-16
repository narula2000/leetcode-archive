# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        def helper(node):
            if node.val == 0 or node.val == 1:
                return node.val == 1
            elif node.val == 2:
                return helper(node.left) or helper(node.right)
            elif node.val == 3:
                return helper(node.left) and helper(node.right)
            else:
                return False
        return helper(root)
