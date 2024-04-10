class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        sorted_deck = sorted(deck)
        que = deque(range(len(deck)))
        print(que)
        ans = [0] * len(deck)

        for card in sorted_deck:
            idx = que.popleft()
            ans[idx] = card
            if que:
                que.append(que.popleft())
        return ans


