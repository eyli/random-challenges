# https://leetcode.com/problems/minimum-difference-in-sums-after-removal-of-elements/

from heapq import *

class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums) // 3
        # The ith element stores the minimum sum that can be obtained by summing n elements
        # from indices 0 to n+i.
        first_mins = []
        # The ith element stores the maximum sum that can be obtained by summing n elements
        # from indices n+i to 3n.
        second_maxes = []

        first_sum = 0
        first_heap = []
        second_sum = 0
        second_heap = []
        for i in range(n):
            first_sum += nums[i]
            first_heap.append(-nums[i])
            second_sum += nums[2*n+i]
            second_heap.append(nums[2*n+i])
        heapify(first_heap)
        heapify(second_heap)

        first_mins.append(first_sum)
        second_maxes.append(second_sum)
        for i in range(n):
            first_current = nums[n+i]
            heappush(first_heap, -first_current)
            first_removed_value = -heappop(first_heap)
            first_sum += (first_current - first_removed_value)
            first_mins.append(first_sum)

            second_current = nums[2*n-1-i]
            heappush(second_heap, second_current)
            second_removed_value = heappop(second_heap)
            second_sum += (second_current - second_removed_value)
            second_maxes.append(second_sum)
        second_maxes.reverse()

        lowest_seen = first_mins[0] - second_maxes[0]
        for i in range(1, len(first_mins)):
            first_min = first_mins[i]
            second_max = second_maxes[i]
            lowest_seen = min(lowest_seen, first_min - second_max)
        return lowest_seen

