# https://leetcode.com/problems/longest-palindrome/

from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        letter_counts = Counter(s)

        output = 0
        has_odd = False

        for letter, count in letter_counts.items():
            if count % 2 == 1:
                has_odd = True
            output += (count // 2) * 2

        if has_odd:
            output += 1
        return output
