class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        lst = list(zip(heights, names))
        lst.sort(reverse=True,key=lambda pair: pair[0])
        return [pair[1] for pair in lst]