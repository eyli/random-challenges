# https://leetcode.com/problems/product-of-array-except-self/

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)

        left_product = 1
        for i, num in enumerate(nums):
            output[i] *= left_product
            left_product *= num
        right_product = 1
        for j in range(len(nums) - 1, -1, -1):
            num = nums[j]
            output[j] *= right_product
            right_product *= num
        return output
