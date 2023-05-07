# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
        if left and right:
            if left.val != right.val:
                return False
            return self.isSameTree(left.left, right.left) and self.isSameTree(left.right, right.right)
        elif not left and not right:
            return True
        else:
            return False
