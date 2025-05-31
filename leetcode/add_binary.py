# https://leetcode.com/problems/add-binary/

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        output_digits = []
        carry = 0
        for i in range(max(len(a), len(b))):
            ia = len(a) - 1 - i
            ib = len(b) - 1 - i

            if ia >= 0 and a[ia] == '1':
                digit_a = 1
            else:
                digit_a = 0

            if ib >= 0 and b[ib] == '1':
                digit_b = 1
            else:
                digit_b = 0

            digit = (digit_a + digit_b + carry) % 2
            carry = (digit_a + digit_b + carry) // 2
            output_digits.append(digit)
        if carry:
            output_digits.append(carry)
        return ''.join(str(digit) for digit in output_digits[::-1])
