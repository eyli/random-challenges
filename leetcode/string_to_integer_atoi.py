# https://leetcode.com/problems/string-to-integer-atoi/

class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if not s:
            return 0

        i = 0
        positive = True
        if s[0] == '-':
            positive = False
            i += 1
        elif s[0] == '+':
            i += 1

        result = 0
        while i < len(s) and s[i].isnumeric():
            result *= 10
            result += int(s[i])
            i += 1
        if not positive:
            result *= -1
        if result > (2 ** 31 - 1):
            return 2 ** 31 - 1
        if result < -2 ** 31:
            return -2 ** 31
        return result
