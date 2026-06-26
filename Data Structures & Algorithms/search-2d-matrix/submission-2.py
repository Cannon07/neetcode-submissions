class Solution:
    def getPossibleRow(self, matrix:List[List[int]], target: int) -> int:
        for i in range(len(matrix)):
            curr_row_max = matrix[i][-1]
            if target <= curr_row_max:
                return i
        return len(matrix) - 1

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_index = self.getPossibleRow(matrix, target)
        row = matrix[row_index]
        left = 0
        right = len(row) - 1

        while left <= right:
            middle = (left + right) // 2
            if row[middle] == target:
                return True
            elif row[middle] < target:
                left = middle + 1
            else:
                right = middle - 1
        return False
        