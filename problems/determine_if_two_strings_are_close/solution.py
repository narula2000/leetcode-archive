class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        counter_1 = Counter(word1)
        counter_2 = Counter(word2)

        if counter_1.keys() != counter_2.keys():
            return False
        if sorted(counter_1.values()) != sorted(counter_2.values()):
            return False

        return True