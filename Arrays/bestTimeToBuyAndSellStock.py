'''
Leetcode #121: Best Time to Buy and Sell Stock
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
Time: O(n) | Space O(1)
'''


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maximumProfit = 0
        minPrice = float('inf')

        for i in range(len(prices)):
            if prices[i] < minPrice:
                minPrice = prices[i]
            if (prices[i] - minPrice) > maximumProfit:
                maximumProfit = prices[i] - minPrice
        return maximumProfit
