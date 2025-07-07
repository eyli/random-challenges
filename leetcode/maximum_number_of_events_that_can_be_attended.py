# https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended/

import heapq

class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        ordered_events = sorted(events, key=lambda x: (x[0], x[1]))

        attended = 0
        latest = 0
        i = 0
        overlapping_events = []

        while i < len(ordered_events) or overlapping_events:
            if not overlapping_events:
                latest = max(latest, ordered_events[i][0])

            while i < len(ordered_events) and ordered_events[i][0] <= latest:
                start, end = ordered_events[i]
                heapq.heappush(overlapping_events, end)
                i += 1

            while overlapping_events and overlapping_events[0] < latest:
                heapq.heappop(overlapping_events)

            if overlapping_events:
                heapq.heappop(overlapping_events)
                attended += 1
                latest += 1

        return attended
