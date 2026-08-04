class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n != 0 and n not in seen:
            seen.add(n)

            curr_sum = 0
            while n:
                digit = n % 10
                curr_sum += digit ** 2

                n = n // 10
            n = curr_sum
        
        return n == 1