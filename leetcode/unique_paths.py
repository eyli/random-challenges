# https://leetcode.com/problems/unique-paths/

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = m + n - 2
        col = min(m, n) - 1

        output = 1
        for i in range(col):
            output *= row - i
            output //= i + 1

        return output
