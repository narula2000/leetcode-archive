# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    accum = 0
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.accum = 0
        self.helper(root, low, high)
        return self.accum
        
    
    def helper(self, node, low, high):
        if not node:
            return

        if high >= node.val >= low:
            self.accum += node.val
        
        self.helper(node.left, low, high)
        self.helper(node.right, low, high)