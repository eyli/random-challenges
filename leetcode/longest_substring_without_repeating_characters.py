class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = {}
        current_start = 0
        max_length = 0

        for i, c in enumerate(s):
            if c in last_seen:
                current_start = max(current_start, last_seen[c] + 1)
            last_seen[c] = i
            current_length = i - current_start + 1
            max_length = max(current_length, max_length)
        return max_length
