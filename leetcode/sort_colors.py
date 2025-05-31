# https://leetcode.com/problems/sort-colors/

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeros_index = 0
        ones_index = 0
        twos_index = len(nums) - 1

        while ones_index <= twos_index:
            num = nums[ones_index]
            if num == 0:
                nums[zeros_index], nums[ones_index] = nums[ones_index], nums[zeros_index]
                zeros_index += 1
                ones_index += 1
            elif num == 1:
                ones_index += 1
            elif num == 2:
                nums[ones_index], nums[twos_index] = nums[twos_index], nums[ones_index]
                twos_index -= 1
