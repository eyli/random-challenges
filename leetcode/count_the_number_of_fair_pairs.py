# https://leetcode.com/problems/count-the-number-of-fair-pairs/

class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        sorted_nums = sorted(nums)
        i = 0
        j = len(sorted_nums) - 1

        total_pairs = 0
        j_lower = None
        j_upper = None
        while i < j:
            curr_sum = sorted_nums[i] + sorted_nums[j]
            if curr_sum >= lower and curr_sum <= upper:
                j_upper = j
                if j_lower is None:
                    j_lower = j # could do binary search here, for later
                if j_lower < i:
                    j_lower = i

                lower_sum = sorted_nums[i] + sorted_nums[j_lower]
                while lower_sum >= lower and j_lower > i:
                    j_lower -= 1
                    lower_sum = sorted_nums[i] + sorted_nums[j_lower]
                total_pairs += j_upper - j_lower
                i += 1
            elif curr_sum < lower:
                i += 1
            else:
                j -= 1
        return total_pairs
