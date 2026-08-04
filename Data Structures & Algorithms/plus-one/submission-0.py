class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        sum = ""
        for digit in digits:
            sum += str(digit)
        
        num = int(sum) + 1
        return [int(n) for n in str(num) ]