# https://leetcode.com/problems/rank-transform-of-an-array/

class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        ordered = sorted(set(arr))
        value_to_rank = {}
        for i, elem in enumerate(ordered):
            value_to_rank[elem] = i + 1
        return [value_to_rank[elem] for elem in arr]
