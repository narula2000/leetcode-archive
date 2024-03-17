class Solution:
    def insert(self, lst: List[List[int]], interval: List[int]) -> List[List[int]]:
        result, i = [], 0

        while i < len(lst) and lst[i][1] < interval[0]: # Find lower Bound
            result.append(lst[i])
            i += 1
        
        while i < len(lst) and lst[i][0] <= interval[1]: # Merge intersections
            interval = [min(interval[0], lst[i][0]), max(interval[1], lst[i][1])]
            i += 1
        result.append(interval)
        
        while i < len(lst): # Find upper Bound
            result.append(lst[i])
            i += 1
        
        return result 
