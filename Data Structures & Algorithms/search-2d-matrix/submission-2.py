class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        total = rows * cols

        left = 0
        right = total - 1
        while left <= right:
            mid = left + (right - left) // 2
            row = mid // cols
            col = mid % cols

            if target > matrix[row][col]:
                left = mid + 1
            elif target < matrix[row][col]:
                right = mid - 1
            else:
                return True
        return False
