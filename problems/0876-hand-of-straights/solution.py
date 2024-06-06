class Solution:
    def isNStraightHand(self, hands: List[int], gs: int) -> bool:
        if len(hands) % gs:
            return False
        counter = Counter(hands)
        keys = sorted(counter.keys())
        for key in keys:
            if counter[key] > 0:
                for i in range(1, gs):
                    if counter[key+i] < counter[key]:
                        return False
                    counter[key+i] -= counter[key]
        return True

