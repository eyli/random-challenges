# https://leetcode.com/problems/find-lucky-integer-in-an-array/

from collections import Counter

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        return max((x for x, count in Counter(arr).items() if x == count), default=-1)
