# https://leetcode.com/problems/partition-equal-subset-sum/

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        target = total // 2

        summable = [False] * (target + 1)
        summable[0] = True

        for num in nums:
            for i in range(target, num - 1, -1):
                if summable[i - num]:
                    if i == target:
                        return True
                    summable[i] = True
        return False
