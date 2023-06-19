class Solution:
    def largestAltitude(self, gains: List[int]) -> int:
        current_altitude, max_altitude = 0, 0
        for gain in gains:
            current_altitude += gain
            max_altitude = max(max_altitude, current_altitude)
        
        return max_altitude