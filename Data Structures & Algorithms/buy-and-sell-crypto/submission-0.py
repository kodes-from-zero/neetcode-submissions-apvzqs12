class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max = 0
        for price in prices:
            if price < min_price:
                min_price = price
            profit = price - min_price
            if(profit > max):
                max = profit
        return max
        