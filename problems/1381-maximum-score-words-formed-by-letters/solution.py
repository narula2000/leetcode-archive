class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        def helper(n, letter):
            if len(words) == n: return 0
            ans, copy = 0, letter
            for i in words[n]:
                if i not in copy: return helper(n+1, letter)
                copy = copy.replace(i, "", 1)
                ans += score[ord(i) - ord("a")]
            return max(helper(n+1, letter), ans+helper(n+1, copy))
        return helper(0, "".join(letters))

