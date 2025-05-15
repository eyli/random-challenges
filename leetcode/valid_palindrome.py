# https://leetcode.com/problems/valid-palindrome/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_string = ''.join(char.lower() for char in s if char.isalnum())
        i = 0
        j = len(cleaned_string) - 1
        while i < j:
            if cleaned_string[i] != cleaned_string[j]:
                return False
            i += 1
            j -= 1
        return True
