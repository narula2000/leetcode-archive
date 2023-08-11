class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        hash = [0] * (amount + 1)
        hash[0] = 1

        for coin in coins:
            for i in range(coin, amount + 1):
                hash[i] += hash[i - coin]
        
        return hash[amount]
