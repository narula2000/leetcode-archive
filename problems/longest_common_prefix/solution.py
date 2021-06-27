class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs == []:
            return ""
        elif len(strs) == 1:
            return strs[0]
        else:
            template = min(strs, key=len)
            strs.remove(template)
            flag = True
            ans = ""
            for i, val in enumerate(template):
                for string in strs:
                    if string[i] != val:
                        flag = False
                        break
                if flag:
                    ans += val
                else:
                    break
            return ans