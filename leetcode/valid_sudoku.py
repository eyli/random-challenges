# https://leetcode.com/problems/valid-sudoku/

from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows_seen = defaultdict(set) # mapping from (row: int -> seen_ints: Set[int])
        cols_seen = defaultdict(set) # mapping from (col: int -> seen_ints: Set[int])
        cells_seen = defaultdict(set) # mapping from (cell: int -> seen_ints: Set[int])

        for i in range(len(board)):
            for j in range(len(board[0])):
                val = board[i][j]
                if val == '.':
                    continue
                cell = (i // 3) * 3 + j // 3
                if val in rows_seen[i] or val in cols_seen[j] or val in cells_seen[cell]:
                    return False
                rows_seen[i].add(val)
                cols_seen[j].add(val)
                cells_seen[cell].add(val)
        return True
