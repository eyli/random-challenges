# https://leetcode.com/problems/word-search/

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        NEIGHBORS = [
            (1, 0),
            (0, 1),
            (-1, 0),
            (0, -1),
        ]

        def dfs(i, j, remaining_word, visited):
            if not remaining_word:
                return True

            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
                return False
            if (i, j) in visited:
                return False
            if board[i][j] != remaining_word[0]:
                return False

            visited.add((i, j))
            for dr, dc in NEIGHBORS:
                if dfs(i+dr, j+dc, remaining_word[1:], visited):
                    return True
            visited.remove((i, j))
            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, word, set()):
                    return True

        return False
