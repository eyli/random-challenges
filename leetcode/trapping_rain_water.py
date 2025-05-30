# https://leetcode.com/problems/trapping-rain-water/

class Solution:
    def trap(self, heights: List[int]) -> int:
        total_water = 0

        left_wall = 0
        left_wall_index = -1
        current_water = 0
        for i in range(len(heights)):
            height = heights[i]
            if height >= left_wall:
                total_water += current_water
                current_water = 0
                left_wall = height
                left_wall_index = i
            else:
                current_water += left_wall - height

        right_wall = 0
        current_water = 0
        for j in range(len(heights) - 1, left_wall_index - 1, -1):
            height = heights[j]
            if height >= right_wall:
                total_water += current_water
                current_water = 0
                right_wall = height
            else:
                current_water += right_wall - height

        return total_water
