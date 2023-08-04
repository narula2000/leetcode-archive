class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        def constructor(curr, memo):
            if curr in memo:
                return memo[curr]
            
            if not curr:
                return True
            
            for word in wordDict:
                if curr.startswith(word):
                    new = curr[len(word):] # Word left to compute
                    if constructor(new, memo):
                        memo[curr] = True
                        return True
            
            memo[curr] = False
            return False
        
        return constructor(s, dict())