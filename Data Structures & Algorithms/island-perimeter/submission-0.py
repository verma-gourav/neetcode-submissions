class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        visited = set()

        def dfs(row, col):
            if (row < 0 or row >= ROWS or col < 0 or col >= COLS or 
            grid[row][col] == 0):
                return 1
            
            if (row, col) in visited:
                return 0
            
            visited.add((row, col))
            perim = 0
            for dr, dc in directions:
                perim += dfs(row + dr, col + dc)
            
            return perim
        
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col]:
                    return dfs(row, col)
        
        return 0
