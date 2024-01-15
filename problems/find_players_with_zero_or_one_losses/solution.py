class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winner, loser, table = [], [], dict()

        for win, lose in matches:
            table[win] = table.get(win, 0)
            table[lose] = table.get(lose, 0) + 1
        
        for k, v in table.items():
            if v == 0:
                winner.append(k)
            if v == 1:
                loser.append(k)
        
        return [sorted(winner), sorted(loser)]
