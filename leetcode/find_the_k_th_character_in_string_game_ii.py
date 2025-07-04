# https://leetcode.com/problems/find-the-k-th-character-in-string-game-ii

class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        num_characters = pow(2, len(operations))
        current_k = k - 1
        increments = 0
        for operation in operations[::-1]:
            num_characters //= 2
            if operation == 1 and current_k >= num_characters:
                increments = (increments + 1) % 26
            current_k %= num_characters

        return chr(ord('a') + increments)
