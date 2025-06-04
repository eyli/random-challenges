# https://leetcode.com/problems/longest-palindromic-substring/

class Solution:
    def longestPalindrome(self, s: str) -> str:

        longest_seen = ""
        for i in range(len(s) * 2 - 1):
            center = i // 2
            pair_center = (i % 2) == 1

            l = center
            r = center
            if pair_center:
                r += 1
            while l >= 0 and r < len(s):
                if s[l] != s[r]:
                    break
                l -= 1
                r += 1
            l += 1
            r -= 1
            if r - l + 1 > len(longest_seen):
                longest_seen = s[l:r+1]

        return longest_seen
