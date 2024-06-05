class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        memo = Counter(words[0])
        for word in words:
            memo &= Counter(word)
        return list(memo.elements())
