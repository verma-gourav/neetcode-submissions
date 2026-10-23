class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        count = {n : 0 for n in nums}
        for num in nums:
            count[num] += 1
        
        def backtrack(perm):
            if len(perm) == len(nums):
                res.append(perm.copy())
                return
            
            for n in count:
                if count[n] > 0:
                    perm.append(n)
                    count[n] -= 1

                    backtrack(perm)

                    perm.pop()
                    count[n] += 1
        
        backtrack([])
        return res