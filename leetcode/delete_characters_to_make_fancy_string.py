# https://leetcode.com/problems/delete-characters-to-make-fancy-string/

class Solution:
    def makeFancyString(self, s: str) -> str:
        output = []
        for i, c in enumerate(s):
            if i < 2 or (s[i] != s[i-2] or s[i] != s[i-1]):
                output.append(c)
        return ''.join(output)
