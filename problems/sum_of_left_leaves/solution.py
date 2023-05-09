# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    result = 0 
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def helper(tree, isRight=False):
            if not tree:
                return
            if not tree.left and not tree.right and not isRight:
                self.result += tree.val
                return
            helper(tree.left)
            helper(tree.right, True)
        helper(root, True) 
        return self.result