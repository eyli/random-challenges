# https://leetcode.com/problems/valid-word/

class Solution:
    def isValid(self, word: str) -> bool:
        VOWELS = 'aeiou'
        has_vowel = False
        has_consonant = False
        if len(word) < 3:
            return False
        for c in word:
            if not c.isalnum():
                return False
            if c.lower() in VOWELS:
                has_vowel = True
            elif c.isalpha():
                has_consonant = True
        return has_vowel and has_consonant
