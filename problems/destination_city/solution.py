class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        mapper = dict()
        for city_a, city_b in paths:
            mapper[city_a] = city_b
        for _, val in mapper.items():
            if val not in mapper.keys():
                return val