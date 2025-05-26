# https://leetcode.com/problems/climbing-stairs/

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return 1
        curr_val = 2
        prev_val = 1
        for i in range(2, n):
            next_val = prev_val + curr_val
            prev_val = curr_val
            curr_val = next_val
        return curr_val
