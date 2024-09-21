# https://leetcode.com/problems/lexicographical-numbers/

class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        output = []
        current = 1
        for i in range(n):
            output.append(current)
            if current * 10 <= n:
                current *= 10
            else:
                if current >= n:
                    current //= 10
                current += 1
                while current % 10 == 0:
                    current //= 10
        return output
