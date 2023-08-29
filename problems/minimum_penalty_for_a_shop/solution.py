class Solution:
    def bestClosingTime(self, customers: str) -> int:
        N = len(customers)
        idx, max_score, score = -1, 0, 0

        for i in range(N):
            if customers[i] == 'Y':
                score += 1
            else:
                score -= 1
            
            if score > max_score:
                max_score = score
                idx = i
        
        return idx + 1