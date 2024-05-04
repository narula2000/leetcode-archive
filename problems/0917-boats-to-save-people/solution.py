class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        ans, l, r = 0, 0, len(people)-1
        while l <= r:
            ans += 1
            if people[l] + people[r] <= limit:
                l += 1
            r -= 1
        return ans
