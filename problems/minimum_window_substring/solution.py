class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        
        dic = defaultdict(int)
        for char in t:
            dic[char] += 1
        
        req = len(dic)
        l = r = formed = 0

        window = defaultdict(int)
        ans = [-1, 0, 0]
        while r < len(s):
            k = s[r]
            window[k] += 1

            if k in dic and window[k] == dic[k]:
                formed += 1
            while l <= r and formed == req:
                k = s[l]
                if ans[0] == -1 or r - l+1 < ans[0]:
                    ans[0] = r - l+1
                    ans[1] = l
                    ans[2] = r
                window[k] -= 1
                if k in dic and window[k] < dic[k]:
                    formed -= 1
                l += 1
            r += 1
        return "" if ans[0] == -1 else s[ans[1]:ans[2]+1]