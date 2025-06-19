# https://leetcode.com/problems/divide-array-into-arrays-with-max-difference/

class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums = sorted(nums)
        output = []
        for i in range(len(nums) // 3):
            start = 3 * i
            end = 3 * (i + 1)
            segment = nums[start:end]
            if segment[2] - segment[0] > k:
                return []
            output.append(segment)

        return output
