# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        paths = []
        def helper(node, path):
            if not node:
                return
            tmp = path + [str(node.val)]
            if not node.left and not node.right: # leaf node
                paths.append(tmp)
            else: # not leaf
                helper(node.left, tmp)
                helper(node.right, tmp)
        helper(root, []) 
        return ["->".join(path) for path in paths]
        