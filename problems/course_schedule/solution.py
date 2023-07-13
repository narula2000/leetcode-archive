class Solution:
    def canFinish(self, num_c: int, prerequisites: List[List[int]]) -> bool:
        def build_list(n, edge_lst):
            lst = [[] for _ in range(n)]

            for a, b in edge_lst: # (a_i, b_i)
                lst[b].append(a)
            
            return lst
        
        lst = build_list(num_c,  prerequisites)
        state = [0] * num_c

        def have_cycle(node):
            if state[node] == 1:
                return False
            elif state[node] == -1:
                return True
            else:
                state[node] = -1
                for i in lst[node]:
                    if have_cycle(i):
                        return True
                
                state[node] = 1
                return False
        

        for node in range(num_c):
            if have_cycle(node):
                return False
        
        return True