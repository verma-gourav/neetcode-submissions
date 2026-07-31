class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)
        seen = set()
        min_heap = [[grid[0][0], 0 , 0]] # [time/height, row, col]
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        seen.add((0, 0))
        while min_heap:
            t, r, c = heapq.heappop(min_heap)
            if r == N - 1 and c == N - 1:
                return t
            
            for dr, dc in directions:
                neig_r, neig_c = r + dr, c + dc
                if (neig_r < 0 or neig_c < 0 or neig_r == N or neig_c == N or 
                    (neig_r, neig_c) in seen):
                    continue
                seen.add((neig_r, neig_c))
                heapq.heappush(min_heap,
                [max(t, grid[neig_r][neig_c]), neig_r, neig_c])
            