# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        highest_profit_seen = 0
        if prices:
            lowest_seen = prices[0]
            for price in prices[1:]:
                highest_profit_seen = max(highest_profit_seen, price - lowest_seen)
                lowest_seen = min(lowest_seen, price)
        return highest_profit_seen
