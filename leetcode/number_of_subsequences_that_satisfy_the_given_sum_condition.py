# https://leetcode.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/

class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        MOD = 10 ** 9 + 7
        sorted_nums = sorted(nums)

        powers_two = [1] * len(nums)
        for i in range(1, len(powers_two)):
            powers_two[i] = (powers_two[i-1] * 2) % MOD

        output = 0
        j = len(sorted_nums) - 1
        for i, num in enumerate(sorted_nums):
            while j >= i and sorted_nums[j] + num > target:
                j -= 1

            if j >= i:
                output = (output + powers_two[j - i]) % MOD

        return output
