class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        def helper(i):
            return (mat[i], i)
        rows = sorted(range(len(mat)), key=helper)
        del rows[k:]
        return rows