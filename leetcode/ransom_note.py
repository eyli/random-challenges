# https://leetcode.com/problems/ransom-note/

from collections import defaultdict

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_counter = defaultdict(int)
        for letter in magazine:
            magazine_counter[letter] += 1
        for letter in ransomNote:
            if not magazine_counter[letter]:
                return False

            magazine_counter[letter] -= 1

        return True
