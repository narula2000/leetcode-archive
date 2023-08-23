class Solution:
    def reorganizeString(self, s: str) -> str:
        N, counter = len(s), Counter(s)
        min_heap = [(-count, char) for char, count in counter.items()]
        heapq.heapify(min_heap)
        
        prev = None
        result = ""

        while prev or min_heap:
            if prev and not min_heap: # Repeating value
                return ""
            
            count, char = heapq.heappop(min_heap)

            result += char
            count += 1

            if prev:
                heapq.heappush(min_heap, prev)
                prev = None
            
            if count != 0: # Check if the char is all used up
                prev = (count, char)
        
        return result
