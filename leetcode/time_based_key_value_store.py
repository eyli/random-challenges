# https://leetcode.com/problems/time-based-key-value-store/

class TimeMap:
    def __init__(self):
        self.store = {} # mapping of key => List<timestamp, value>


    def set(self, key: str, value: str, timestamp: int) -> None:
        values_with_timestamps = self.store.setdefault(key, [])
        values_with_timestamps.append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""

        values_with_timestamps = self.store[key]
        left = 0
        right = len(values_with_timestamps) - 1
        output = ""
        while left <= right:
            mid = left + (right - left) // 2
            if timestamp >= values_with_timestamps[mid][0]:
                left = mid + 1
                output = values_with_timestamps[mid][1]
            else:
                right = mid - 1
        return output
