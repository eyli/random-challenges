# https://leetcode.com/problems/maximum-manhattan-distance-after-k-changes/

class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        ns = 0
        ew = 0

        output = 0
        for i, step in enumerate(s):
            if step == 'N':
                ns += 1
            elif step == 'S':
                ns -= 1
            elif step == 'E':
                ew += 1
            elif step == 'W':
                ew -= 1
            else:
                raise("Unexpected input")

            distance = abs(ns) + abs(ew)
            distance_with_corrections = min(i+1, distance + 2 * k)
            output = max(output, distance_with_corrections)
        return output
