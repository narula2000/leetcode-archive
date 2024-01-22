class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        set_jewels = set(jewels)
        return sum(1 for stone in stones if stone in set_jewels)