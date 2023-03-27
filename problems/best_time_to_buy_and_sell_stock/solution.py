class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_gap = 0
        for price in prices:
            if min_price > price:
                min_price = price
            elif price - min_price > max_gap:
                max_gap = price - min_price
        return max_gap