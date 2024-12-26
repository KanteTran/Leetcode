#https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description            
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max, min, sum = 0, prices[0], 0
        n = len(prices)
        for i in range(1,n):
            if prices[i] < min:
                min = prices[i]
            elif i < n-1 and prices[i+1] < prices[i]: 
                sum+=prices[i] - min
                min = prices[i]
                max = 0
            elif prices[i] - min > max:
                max = prices[i] - min
        
        return sum + max