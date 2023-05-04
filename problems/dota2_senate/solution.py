class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        N = len(senate)

        r = deque()
        d = deque()

        for i, val in enumerate(senate):
            if val == 'R':
                r.append(i)
            else:
                d.append(i)

        
        while r and d:

            r_turn = r.popleft()
            d_turn = d.popleft()

            # Lower index ban higher index
            if r_turn < d_turn:
                r.append(r_turn + N) # Shift voted senate to next round
            else:
                d.append(d_turn + N) # Shift voted senate to next round

        
        return 'Radiant' if r else 'Dire'