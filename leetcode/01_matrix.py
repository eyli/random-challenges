# https://leetcode.com/problems/01-matrix/

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows = len(mat)
        cols = len(mat[0])

        output = [[float('inf')] * cols for _ in range(rows)]

        current_set = set()
        next_set = set()
        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 0:
                    current_set.add((i, j))

        current_distance = 0
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        while current_set:
            for row, col in current_set:
                if row < 0 or row >= rows or col < 0 or col >= cols:
                    continue
                if current_distance < output[row][col]:
                    output[row][col] = current_distance
                    for dr, dc in directions:
                        next_set.add((row+dr, col+dc))
            current_set = next_set
            current_distance += 1
            next_set = set()

        return output
