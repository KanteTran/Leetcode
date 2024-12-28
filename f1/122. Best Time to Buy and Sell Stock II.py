class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        for i in range(1, len(prices)):
            profit = prices[i] - prices[i - 1]
            res += profit if profit > 0 else 0

        return res
