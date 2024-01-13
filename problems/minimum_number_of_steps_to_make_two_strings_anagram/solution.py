class Solution:
    def minSteps(self, s: str, t: str) -> int:
        diff = Counter(t) - Counter(s)
        return sum(v for v in diff.values())