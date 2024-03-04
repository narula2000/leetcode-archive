class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        score = 0
        tokens.sort()
        que = deque(tokens)

        while que:
            if power >= que[0]:
                power -= que.popleft()
                score += 1
            elif len(que) > 2 and score > 0:
                power += que.pop()
                score -= 1
            else:
                return score
        return score