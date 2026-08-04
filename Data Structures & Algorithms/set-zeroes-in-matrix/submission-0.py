class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        mark = [[matrix[r][c] for c in range(len(matrix[0]))] for r in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    for col in range(len(matrix[0])):
                        mark[i][col] = 0
                    for row in range(len(matrix)):
                        mark[row][j] = 0
        
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                matrix[r][c] = mark[r][c]


        