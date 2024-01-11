# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, node: Optional[TreeNode]) -> int:
        return self.dfs(node, node.val, node.val)

    def dfs(self, node, _min, _max):
        if not node:
            return 0

        val = node.val 
        ans = max(abs(val - _min), abs(val - _max))

        _min, _max = min(_min, val), max(_max, val)

        return max(ans, self.dfs(node.left, _min, _max), self.dfs(node.right, _min, _max))
