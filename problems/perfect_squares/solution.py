class Solution:
    def numSquares(self, n: int) -> int:
        if n < 2:
            return n

        lst = [i*i for i in range(n) if i*i <= n]

        ans = 0
        hash_set = set([n])
        while hash_set:
            ans += 1
            tmp = set()
            for to_check in hash_set:
                for square in lst:
                    if to_check == square:
                        return ans
                    if to_check < square: # Went over the n
                        break
                    tmp.add(to_check - square)
                hash_set = tmp
        
        return ans