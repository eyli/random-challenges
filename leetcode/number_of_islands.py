# https://leetcode.com/problems/number-of-islands/

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        num_islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                cell = grid[i][j]
                if cell == '1':
                    num_islands += 1
                    self._color_island(grid, i, j)
        return num_islands

    def _color_island(self, grid, i, j):
        to_color = {(i, j)}
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while to_color:
            row, col = to_color.pop()
            if row >= 0 and row < len(grid) and col >= 0 and col < len(grid[0]) and grid[row][col] == '1':
                grid[row][col] = '2'
                for dr, dc in directions:
                    to_color.add((row+dr, col+dc))
