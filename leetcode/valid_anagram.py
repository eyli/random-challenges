# https://leetcode.com/problems/valid-anagram/

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        char_counts = {}
        for c in s:
            char_counts[c] = char_counts.get(c, 0) + 1
        for c in t:
            if not char_counts.get(c, 0):
                return False
            char_counts[c] -= 1

        return True
