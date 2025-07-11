# https://leetcode.com/problems/find-all-anagrams-in-a-string/

from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_counts = Counter(p)
        window_counts = Counter(s[:len(p)])

        matches = 0
        for c, count in p_counts.items():
            if window_counts[c] >= count:
                matches += 1

        output = []
        if matches == len(p_counts):
            output.append(0)

        for i in range(1, len(s) - len(p) + 1):
            deleted = s[i-1]
            added = s[i+len(p)-1]
            if window_counts[deleted] == p_counts[deleted]:
                matches -= 1
            window_counts[deleted] -= 1
            window_counts[added] += 1
            if window_counts[added] == p_counts[added]:
                matches += 1
            if matches == len(p_counts):
                output.append(i)
        return output
