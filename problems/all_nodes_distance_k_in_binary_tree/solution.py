# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        def generate_parent_map(node, parent):
            if not node:
                return
            
            parent_map[node] = parent

            generate_parent_map(node.left, node)
            generate_parent_map(node.right, node)
        
        def get_nodes(node, distance):
            if not node or node in visited or distance > k:
                return

            visited.add(node) 
            if distance == k:
                result.append(node.val)

            get_nodes(node.left, distance + 1)
            get_nodes(node.right, distance + 1)
            get_nodes(parent_map[node], distance + 1)
        
        parent_map, visited, result = dict(), set(), []

        generate_parent_map(root, None)
        get_nodes(target, 0)

        return result