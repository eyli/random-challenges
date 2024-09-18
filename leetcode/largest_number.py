# https://leetcode.com/problems/largest-number/

import functools

def compare(digits1: str, digits2: str):
    sum1 = digits1 + digits2
    sum2 = digits2 + digits1
    if sum1 > sum2:
        return 1
    elif sum1 < sum2:
        return -1
    else:
        return 0

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        sorted_digits = sorted(
            [str(num) for num in nums],
            key=functools.cmp_to_key(compare),
            reverse=True
        )
        joined = ''.join(sorted_digits)
        if not joined or joined[0] == '0':
            return '0'
        else:
            return joined
