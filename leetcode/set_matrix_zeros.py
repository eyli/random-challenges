# https://leetcode.com/problems/set-matrix-zeroes/

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        first_col_zero = False
        first_row_zero = False
        for j in range(len(matrix[0])):
            current = matrix[0][j]
            if current == 0:
                first_row_zero = True
                break

        # Scan the first col:
        for i in range(len(matrix)):
            current = matrix[i][0]
            if current == 0:
                first_col_zero = True
                break

        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                current = matrix[i][j]
                print(f"{i}, {j}: {current}")
                if current == 0:
                    # Store that the row should be zero'd.
                    matrix[i][0] = 0
                    # Store that the col should be zero'd.
                    matrix[0][j] = 0

        for j in range(1, len(matrix[0])):
            current = matrix[0][j]
            if current == 0:
                for i in range(len(matrix)):
                    matrix[i][j] = 0
        for i in range(1, len(matrix)):
            current = matrix[i][0]
            if current == 0:
                for j in range(len(matrix[0])):
                    matrix[i][j] = 0
        if first_col_zero:
            for i in range(len(matrix)):
                matrix[i][0] = 0
        if first_row_zero:
            for j in range(len(matrix[0])):
                matrix[0][j] = 0
