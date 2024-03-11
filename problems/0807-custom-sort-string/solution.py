class Solution:
    def customSortString(self, order: str, s: str) -> str:
        hash = defaultdict(int)

        for i, val in enumerate(order):
            hash[val] = i

        return "".join(sorted(s, key=lambda val: hash.get(val, float('inf'))))
