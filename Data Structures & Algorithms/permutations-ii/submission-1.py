class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        seen = set()
        nums.sort()

        def backtrack(curr_perm):
            if len(curr_perm) == len(nums):
                res.append(curr_perm.copy())
            
            for i in range(len(nums)):
                if i in seen: 
                    continue
                
                # If this number is identical to the previous one, and the previous 
                # one hasn't been used yet in this branch, skip it to avoid duplicate trees.
                if i > 0 and nums[i] == nums[i - 1] and (i - 1) not in seen:
                    continue
                
                curr_perm.append(nums[i])
                seen.add(i)

                backtrack(curr_perm)

                curr_perm.pop()
                seen.remove(i)
        
        backtrack([])
        return res