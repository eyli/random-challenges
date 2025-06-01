# https://leetcode.com/problems/word-break/

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        longest_word = max(len(word) for word in wordDict)
        words_set = set(wordDict)

        cached_results = {}

        def helper(s, words, i):
            if i == len(s):
                return True
            if i in cached_results:
                return cached_results[i]

            j = i + 1
            while j <= len(s) and j - i <= longest_word:
                candidate = s[i:j]
                if candidate in words_set:
                    result = helper(s, words, j)
                    if result:
                        cached_results[i] = True
                        return True
                j += 1
            cached_results[i] = False
            return False

        return helper(s, words_set, 0)
