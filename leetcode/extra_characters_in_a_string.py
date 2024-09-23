# https://leetcode.com/problems/extra-characters-in-a-string/

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        self.dictionary = set(dictionary)
        return self.minExtraCharHelper(s, 0, {})

    def minExtraCharHelper(self, s, start=0, memoized={}):
        if len(s) - start <= 0:
            return 0

        if start in memoized:
            return memoized[start]

        min_so_far = len(s) - start
        for i in range(start+1, len(s)+1):
            if s[start:i] in self.dictionary:
                candidate = self.minExtraCharHelper(s, i, memoized)
                min_so_far = min(min_so_far, candidate)

        candidate = self.minExtraCharHelper(s, start+1, memoized) + 1
        min_so_far = min(min_so_far, candidate)

        memoized[start] = min_so_far
        return min_so_far
