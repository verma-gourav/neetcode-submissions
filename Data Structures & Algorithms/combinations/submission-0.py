class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def backtrack(start, curr_subset):
            if len(curr_subset) == k:
                res.append(curr_subset.copy())
            
            for i in range(start, n + 1):
                curr_subset.append(i)
                backtrack(i + 1, curr_subset)
                curr_subset.pop()
            
        backtrack(1, [])
        return res