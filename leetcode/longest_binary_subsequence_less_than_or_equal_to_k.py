# https://leetcode.com/problems/longest-binary-subsequence-less-than-or-equal-to-k/

class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        included = 0
        current_value = 0
        digit_value = 1

        for digit in s[::-1]:
            if digit == '0':
                included += 1
                digit_value *= 2
            else:
                if k - current_value >= digit_value:
                    included += 1
                    current_value += digit_value
                    digit_value *= 2
        return included
