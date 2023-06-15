# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        result, level = 0, 0
        max_sum = float('-inf')

        que = collections.deque()
        que.append(root)

        while que:
            level += 1
            level_sum = 0

            for _ in range(len(que)):
                node = que.popleft()
                level_sum += node.val

                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
            
            if max_sum < level_sum:
                max_sum = level_sum
                result = level
        
        return result