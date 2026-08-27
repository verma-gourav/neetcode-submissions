class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        res = []

        for a in asteroids:
            while res and a < 0 and res[-1] > 0:
                if abs(a) > res[-1]:
                    res.pop()
                elif abs(a) < res[-1]:
                    a = 0
                else:
                    a = 0
                    res.pop()
            
            if a:
                res.append(a)
        
        return res

            


                
                