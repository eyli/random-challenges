# https://leetcode.com/problems/palindrome-pairs/

class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        word_dict = {}
        for i, word in enumerate(words):
            word_dict[word] = i

        output = []
        for i, word in enumerate(words):
            for j in range(len(word) + 1):
                left_substr = word[:j]
                right_substr = word[j:]
                if left_substr and isPalindrome(left_substr):
                    pair = right_substr[::-1]
                    if pair in word_dict and word_dict[pair] != i:
                        output.append([word_dict[pair], i])
                if isPalindrome(right_substr):
                    pair = left_substr[::-1]
                    if pair in word_dict and word_dict[pair] != i:
                        output.append([i, word_dict[pair]])
        return output

def isPalindrome(s):
    return s == s[::-1]
