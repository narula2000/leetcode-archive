class Solution:
    def average(self, salary: List[int]) -> float:
        _min = min(salary)
        _max = max(salary)
        avg = 0
        for num in salary:
            if num != _min and num != _max:
                avg += num
        
        return avg / (len(salary) - 2)