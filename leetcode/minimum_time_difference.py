# https://leetcode.com/problems/minimum-time-difference

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        minutes = [int(timePoint[0:2]) * 60 + int(timePoint[3:5]) for timePoint in timePoints]

        minutes.sort()

        minDifference = 24 * 60
        for i in range(len(minutes)):
            curr_val = minutes[i]
            next_val = minutes[(i + 1) % len(minutes)]
            curr_difference = (next_val - curr_val) % 1440
            minDifference = min(minDifference, curr_difference)
        return minDifference
