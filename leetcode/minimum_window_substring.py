# https://leetcode.com/problems/minimum-window-substring/

from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Get all the character counts of t.
        quota = Counter(t)
        important_characters = set(quota)
        surplus = {c: 0 for c in important_characters}

        # Find the leftmost window where t is contained in s.
        left = 0
        right = 0
        while right < len(s) and quota:
            c = s[right]
            if c in important_characters:
                if c in quota:
                    quota[c] -= 1
                    if quota[c] == 0:
                        del(quota[c])
                else:
                    surplus[c] += 1
            right += 1

        if quota:
            return ""

        best_so_far = (left, right)
        while True:
            # Move right pointer forward as much as possible before quota needs to be filled again.
            while not quota:
                print(left, right)
                current_length = best_so_far[1] - best_so_far[0]
                if right - left < current_length:
                    best_so_far = (left, right)
                c_left = s[left]
                if c_left in important_characters:
                    if surplus[c_left] > 0:
                        surplus[c_left] -= 1
                    else:
                        quota[c_left] = 1
                left += 1

            if right < len(s):
                c_right = s[right]
                if c_right in important_characters:
                    if c_right in quota:
                        quota[c_right] -= 1
                        if quota[c_right] == 0:
                            del(quota[c_right])
                    else:
                        surplus[c_right] += 1
                right += 1
            else:
                break

        return s[best_so_far[0]:best_so_far[1]]

