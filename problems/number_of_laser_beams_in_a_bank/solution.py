class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        ans, prev_accum = 0, 0
        for row in bank:
            accum = sum([int(col) for col in row])
            if accum == 0:
                continue

            ans += accum * prev_accum
            prev_accum = accum
        
        return ans