# https://leetcode.com/problems/divisible-and-non-divisible-sums-difference/

class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        return self.arithmetic_sum(n, 1) - 2 * self.arithmetic_sum(n, m)

    def arithmetic_sum(self, max_val, step):
        num_steps = max_val // step
        return (step + num_steps * step) * num_steps // 2
