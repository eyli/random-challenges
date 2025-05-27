# https://leetcode.com/problems/rotting-oranges/

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        total_oranges = 0
        already_rotten = set()
        current_rotten = set()
        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                if cell == 1:
                    total_oranges += 1
                if cell == 2:
                    total_oranges += 1
                    current_rotten.add((i, j))
                    already_rotten.add((i, j))
        if total_oranges == len(already_rotten):
            return 0

        next_rotten = set()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        minutes = 0
        while current_rotten:
            for row, col in current_rotten:
                for dr, dc in directions:
                    if (row+dr >= 0 and
                            row+dr < len(grid) and
                            col+dc >= 0 and
                            col+dc < len(grid[0]) and
                            (row+dr, col+dc) not in already_rotten and
                            grid[row+dr][col+dc] == 1):
                        already_rotten.add((row+dr, col+dc))
                        next_rotten.add((row+dr, col+dc))
            if next_rotten:
                minutes += 1
            current_rotten = next_rotten
            next_rotten = set()
        if total_oranges != len(already_rotten):
            return -1
        else:
            return minutes
