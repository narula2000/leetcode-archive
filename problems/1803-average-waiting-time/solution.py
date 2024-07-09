class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        available_at, total_wait = 0, 0
        for arrival, time in customers:
            available_at = max(available_at, arrival) + time
            total_wait += available_at - arrival
        
        return total_wait / len(customers) 
