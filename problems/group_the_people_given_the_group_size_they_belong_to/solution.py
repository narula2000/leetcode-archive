class Solution:
    def groupThePeople(self, gS: List[int]) -> List[List[int]]:
        hash = collections.defaultdict(list)

        for idx, i in enumerate(gS):
            hash[i].append(idx)
        
        res = []
        for key, lst in hash.items():
            for idx in range(0, len(lst), key):
                res.append(lst[idx:idx+key])
        
        return res