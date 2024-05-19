# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        def dfs(node, parent):
            if not node: return 0
            moves = dfs(node.left, node) + dfs(node.right, node)
            val = node.val - 1
            if parent: parent.val += val
            moves += abs(val)
            return moves
        return dfs(root, None)
