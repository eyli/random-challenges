# https://leetcode.com/problems/candy/

class Solution:
    def candy(self, ratings: List[int]) -> int:
        outputs = [1] * len(ratings)

        chain = 1
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                chain += 1
            else:
                chain = 1
            outputs[i] = chain

        chain = 1
        for i in range(len(ratings) - 2, -1, -1):
            if ratings[i] > ratings[i+1]:
                chain += 1
            else:
                chain = 1
            outputs[i] = max(chain, outputs[i])

        return sum(outputs)
