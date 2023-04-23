# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    min_depth = float('inf')
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(visited, node, path):
            if node and node not in visited:
                visited.add(node.val)
                path.append(node.val)
                if not node.left and not node.right:
                    self.min_depth = min(self.min_depth, len(path))
                if node.left:
                    dfs(visited, node.left, path)
                if node.right:
                    dfs(visited, node.right, path)
                path.pop()
        dfs(set(), root, [])

        if isinstance(self.min_depth, float):
            self.min_depth = 0
        return self.min_depth