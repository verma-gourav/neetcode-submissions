class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums) 
        product_without_zeroes = 1
        zero_count = 0

        for num in nums:
            if num == 0:
                zero_count += 1
            else:
                product_without_zeroes *= num

        if zero_count > 1:
            return res
        
        for i in range(len(nums)):
            if zero_count == 1:
                res[i] = product_without_zeroes if nums[i] == 0 else 0
            else:    
                res[i] = product_without_zeroes // nums[i]
        return res