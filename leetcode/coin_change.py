# https://leetcode.com/problems/coin-change/

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        return self._coin_change_helper(coins, amount, {})

    def _coin_change_helper(self, coins, amount, memoized):
        if amount < 0:
            return -1
        if amount == 0:
            return 0
        elif amount in memoized:
            return memoized[amount]
        else:
            values = []
            for coin in coins:
                value = self._coin_change_helper(coins, amount - coin, memoized)
                if value >= 0:
                    values.append(value)
            if not values:
                memoized[amount] = -1
                return -1
            else:
                lowest = min(values)
                memoized[amount] = lowest + 1
                return lowest + 1
