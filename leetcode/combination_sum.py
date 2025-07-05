# https://leetcode.com/problems/combination-sum/

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        all_paths = []
        self._combination_sum_helper(candidates, target, 0, [], all_paths)
        return all_paths

    def _combination_sum_helper(self, candidates, target, start, path, all_paths):
        if target < 0:
            return

        if target == 0:
            all_paths.append(path[:])

        for i in range(start, len(candidates)):
            candidate = candidates[i]
            path.append(candidate)
            self._combination_sum_helper(
                candidates,
                target - candidate,
                i,
                path,
                all_paths
            )
            path.pop()
