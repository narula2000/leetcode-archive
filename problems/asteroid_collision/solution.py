class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            while stack and stack[-1] > 0 and asteroid < 0:
                if stack[-1] + asteroid < 0: # Go Right
                    stack.pop()
                elif stack[-1] + asteroid > 0: # Go Left
                    break
                else: # Destory each other
                    stack.pop()
                    break
            else: # Same path
                stack.append(asteroid)
        return stack