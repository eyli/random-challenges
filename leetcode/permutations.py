# https://leetcode.com/problems/permutations/

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        nums_used = set()
        path = []
        all_permutations = []

        self._backtrack(nums, nums_used, path, all_permutations)

        return all_permutations

    def _backtrack(self, nums, nums_used, path, all_permutations):
        if len(nums_used) == len(nums):
            all_permutations.append(path[:])
            return

        for num in nums:
            if num not in nums_used:
                nums_used.add(num)
                path.append(num)
                self._backtrack(nums, nums_used, path, all_permutations)
                path.pop()
                nums_used.remove(num)
