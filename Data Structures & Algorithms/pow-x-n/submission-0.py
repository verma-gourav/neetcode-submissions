class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(x, n):
            if n == 0: return 1.0
            if x == 0.0 : return 0.0

            res = helper(x * x, n // 2)
            return x * res if n % 2 else res
        
        result = helper(x, abs(n))
        return result if n >= 0 else 1 / result
