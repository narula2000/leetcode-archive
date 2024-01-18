class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        cache = defaultdict(list)

        for word in strs:
            sorted_word = "".join(sorted(word))
            cache[sorted_word].append(word)
        
        return cache.values()