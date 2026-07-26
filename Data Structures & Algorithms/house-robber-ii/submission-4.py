class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        return max(nums[0], self.helper(nums, 1, len(nums) - 1), self.helper(nums, 0, len(nums) - 2))

        
    def helper(self, nums, start, end):
        rob1, rob2 = 0, 0
        
        for i in range(start, end + 1):
            num = nums[i]
            new_rob = max(rob1 + num, rob2)
            rob1 = rob2
            rob2 = new_rob

        return rob2