# https://leetcode.com/problems/reschedule-meetings-for-maximum-free-time-i/

class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        time_gaps = []
        for i in range(len(startTime)):
            if i == 0:
                previous_end = 0
            else:
                previous_end = endTime[i-1]
            current_start = startTime[i]
            time_gaps.append(current_start - previous_end)
        time_gaps.append(eventTime - endTime[-1])

        window_size = k + 1
        current_window = sum(time_gaps[:window_size])
        highest_seen = current_window
        for i in range(1, len(time_gaps) - window_size + 1):
            current_window -= time_gaps[i-1]
            current_window += time_gaps[i+window_size-1]
            highest_seen = max(highest_seen, current_window)
        return highest_seen
