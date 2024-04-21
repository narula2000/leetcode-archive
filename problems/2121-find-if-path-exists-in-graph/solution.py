class Solution:
    def validPath(self, n: int, edges: List[List[int]], src: int, dst: int) -> bool:
        memo = defaultdict(list)
        for i, j in edges:
            memo[i].append(j)
            memo[j].append(i)

        visited = set()
        def dfs(node):
            if node == dst:
                return True
            visited.add(node)
            for j in memo[node]:
                if j not in visited and dfs(j):
                    return True
            return False
        
        return dfs(src) 
