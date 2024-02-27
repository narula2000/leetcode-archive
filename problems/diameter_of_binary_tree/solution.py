# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        result = [0]

        def dfs(node):
            if not node: return -1
            left, right = dfs(node.left), dfs(node.right)
            diameter = left + 1 + right + 1
            result[0] = max(result[0], diameter)
            return 1 + max(left, right)
        dfs(root) 
        return result[0]