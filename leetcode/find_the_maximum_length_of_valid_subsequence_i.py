# https://leetcode.com/problems/find-the-maximum-length-of-valid-subsequence-i

class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        evens = 0
        odds = 0
        switches = 0
        for i in range(len(nums)):
            curr = nums[i]
            if curr % 2 == 0:
                evens += 1
            else:
                odds += 1

            if i > 0:
                prev = nums[i-1]
                if prev % 2 != curr % 2:
                    switches += 1

        return max([evens, odds, switches+1])
