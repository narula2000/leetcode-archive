class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        N = len(candidates)
        def dfs(lst, curr_sum, idx):
            if curr_sum > target:
                return target
            if curr_sum == target:
                result.append(lst)
            for i in range(idx, N):
                dfs(lst+[candidates[i]], curr_sum+candidates[i], i)
        
        dfs([], 0, 0)

        return result
"""
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        dp = [[] for _ in range(target+1)]
        for c in candidates:                                  # O(N): for each candidate
            for i in range(c, target+1):                      # O(M): for each possible value <= target
                if i == c:
                    dp[i].append([c])
                for comb in dp[i-c]:
                    dp[i].append(comb + [c]) # O(M) worst: for each combination
        return dp[-1]
"""