class Solution:
    def frequencySort(self, s: str) -> str:
        count = sorted([[v, k] for k, v in Counter(s).items()], reverse=True)
        return "".join([v[1]*v[0] for v in count])