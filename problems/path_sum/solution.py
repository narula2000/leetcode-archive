# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    FOUND = False
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(visited, node, path):
            if node and node not in visited:
                visited.add(node.val)
                path.append(node.val)

                if node.left:
                    dfs(visited, node.left, path)
                if node.right:
                    dfs(visited, node.right, path)

                isLeaf = False
                if not node.left and not node.right:
                    isLeaf = True

                if isLeaf and sum(path) == targetSum:
                    self.FOUND = True
                path.pop()
        dfs(set(), root, [])
        return self.FOUND 

"""
class EditorialSolution:
    def hasPathSum(self, root, acc):
        if not root:
            return False

        acc -= root.val
        if not root.left and not root.right:  # if reach a leaf
            return acc == 0
        return self.hasPathSum(root.left, acc) or self.hasPathSum(root.right, acc)
"""