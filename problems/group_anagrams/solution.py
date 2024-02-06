class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)

        for word in strs:
            sorted_w = "".join(sorted(word))
            dic[sorted_w].append(word)
        
        return list(dic.values())