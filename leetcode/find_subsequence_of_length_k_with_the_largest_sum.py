# https://leetcode.com/problems/find-subsequence-of-length-k-with-the-largest-sum/

from collections import Counter

class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        # Side note: I know there's a quickselect solution but I can't be bothered.

        counts = Counter(sorted(nums)[-k:])

        output = []
        for num in nums:
            if counts[num]:
                output.append(num)
                counts[num] -= 1
        return output
