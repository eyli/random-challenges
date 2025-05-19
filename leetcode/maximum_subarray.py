# https://leetcode.com/problems/maximum-subarray/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currentSum = 0
        maxSeen = float('-inf')
        for num in nums:
            currentSum += num
            maxSeen = max(currentSum, maxSeen)
            currentSum = max(currentSum, 0)
        return maxSeen
