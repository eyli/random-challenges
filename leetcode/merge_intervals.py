# https://leetcode.com/problems/merge-intervals/

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x: x[0])
        output = []
        left = None
        right = None
        for interval in intervals:
            if left is None:
                left = interval[0]
                right = interval[1]
            elif interval[0] > right:
                output.append([left, right])
                left = interval[0]
                right = interval[1]
            else:
                right = max(right, interval[1])
        if left is not None:
            output.append([left, right])
        return output
