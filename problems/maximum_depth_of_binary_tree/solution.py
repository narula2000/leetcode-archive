# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        def helper(left, right):
            if not left and not right:
                return 1
            elif left and not right:
                return 1 + helper(left.left, left.right)
            elif right and not left:
                return 1 + helper(right.left, right.right)
            else:
                return 1 + max(helper(left.left, left.right),helper(right.left, right.right))
        return helper(root.left, root.right)

"""
class EditorialSolution:
    def maxDepth(self, root):
        stack = []
        if root is not None:
            stack.append((1, root))
        
        depth = 0
        while stack != []:
            current_depth, root = stack.pop()
            if root is not None:
                depth = max(depth, current_depth)
                stack.append((current_depth + 1, root.left))
                stack.append((current_depth + 1, root.right))
        
        return depth
"""