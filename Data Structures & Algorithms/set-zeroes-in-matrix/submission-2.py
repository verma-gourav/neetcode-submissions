class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROWS, COLS = len(matrix), len(matrix[0])

        row, col = [False] * ROWS, [False] * COLS

        for i in range(ROWS):
            for j in range(COLS):
                if matrix[i][j] == 0:
                    row[i] = True
                    col[j] = True
        
        for i in range(ROWS):
            for j in range(COLS):
                if row[i] or col[j]:
                    matrix[i][j] = 0