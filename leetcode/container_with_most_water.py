# https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        biggest_seen = 0

        i = 0
        j = len(heights) - 1

        while i < j:
            left = heights[i]
            right = heights[j]
            water = min(left, right) * (j - i)
            biggest_seen = max(biggest_seen, water)
            if left < right:
                i += 1
            else:
                j -= 1
        return biggest_seen
