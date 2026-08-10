class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = prices[0]
        maxP = 0
        i=0
        while i < len(prices):
            if prices[i] < minPrice:
                minPrice = prices[i]
            next = i+1
            while next < len(prices) and prices[next] > minPrice:
                profit = prices[next] - minPrice
                maxP = max(profit, maxP)
                next=next+1
            i=next
            
        return maxP