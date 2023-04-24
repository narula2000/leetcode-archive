class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            max_1 = max(stones)
            stones.remove(max_1)
            max_2 = max(stones)
            stones.remove(max_2)

            if max_1 and max_2:
                diff = max_1 - max_2
                if diff != 0:
                    stones.append(diff)
        
        return stones[0] if len(stones) == 1 else 0
