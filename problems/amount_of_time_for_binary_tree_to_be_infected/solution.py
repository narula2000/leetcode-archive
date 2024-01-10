# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        G = defaultdict(list)
        stack = [(root, None)]
        while stack:
            node, parent = stack.pop()
            if parent:
                G[parent.val].append(node.val)
                G[node.val].append(parent.val)
            
            if node.left:
                stack.append((node.left, node))
            if node.right:
                stack.append((node.right, node))
        
        ans = -1
        visited = {start}
        que = deque([start])

        while que:
            for _ in range(len(que)):
                node = que.popleft()
                for adj in G[node]:
                    if adj not in visited:
                        visited.add(adj)
                        que.append(adj)
            ans += 1
        
        return ans