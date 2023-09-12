class Solution:
    def minDeletions(self, s: str) -> int:
        counter = Counter(s)
        count, uniq = 0, set()

        for car, freq in counter.items():
            while freq > 0 and freq in uniq:
                freq -= 1
                count += 1
            
            uniq.add(freq)
        
        return count