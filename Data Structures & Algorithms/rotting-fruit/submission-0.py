class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        self.fresh = 0

        def add_grid(r, c):
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] != 1):
                return
            grid[r][c] = 2
            q.append([r, c])
            self.fresh -= 1

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append([r, c])
                elif grid[r][c] == 1:
                    self.fresh += 1
        
        if self.fresh == 0:
            return 0
        
        min = 0
        while q and self.fresh > 0:
            min += 1
            for i in range(len(q)):
                r, c = q.popleft()
                
                add_grid(r + 1, c)
                add_grid(r - 1, c)
                add_grid(r, c + 1)
                add_grid(r, c - 1)
        
        return min if self.fresh == 0 else -1