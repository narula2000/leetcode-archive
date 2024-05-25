class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        def helper(string, counter, memo):
            if string in memo: return memo[string]
            ans = []
            if counter[string] == 1:
                ans = [string]
            
            for i in range(len(string)):
                if counter[string[:i]] == 1:
                    tmp = helper(string[i:], counter, memo)
                    for char in tmp:
                        ans.append(f"{string[:i]} {char}")
            memo[string] = ans
            return ans
        counter = defaultdict(int)
        for key in wordDict:
            counter[key] = 1
        return helper(s, counter, dict())

