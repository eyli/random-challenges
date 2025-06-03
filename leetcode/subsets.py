# https://leetcode.com/problems/subsets/

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def helper(nums, i, output):
            if i >= len(nums):
                return
            num = nums[i]
            for j in range(len(output)):
                elem = output[j]
                new_subset = elem[:] + [num]
                output.append(new_subset)
            helper(nums, i+1, output)

        output = [[]]
        helper(nums, 0, output)
        return output
