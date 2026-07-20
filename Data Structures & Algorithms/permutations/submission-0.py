class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        seen = set()

        def dfs(curr):
            if len(curr) == len(nums):
                res.append(curr.copy())
                return
            
            for num in nums:
                if num in seen:
                    continue
                
                curr.append(num)
                seen.add(num)

                dfs(curr)

                curr.pop()
                seen.remove(num)
        
        dfs([])
        return res