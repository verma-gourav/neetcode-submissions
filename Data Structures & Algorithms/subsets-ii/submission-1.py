class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def dfs(i, curr):
            res.append(curr[::])
            
            for j in range(i, len(nums)):
                if j > i and nums[j] == nums[j - 1]:
                    continue

                curr.append(nums[j])
                dfs(j + 1, curr)
                curr.pop()
        
        dfs(0, [])
        return res