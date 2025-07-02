# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mappings = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }

        def dfs(prefix, remaining_digits, output):
            if not remaining_digits:
                if prefix:
                    output.append(prefix)
            else:
                for letter in mappings[remaining_digits[0]]:
                    dfs(prefix + letter, remaining_digits[1:], output)

        output = []
        dfs('', digits, output)
        return output
