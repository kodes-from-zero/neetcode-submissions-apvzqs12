class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = prices[0]
        maxP=0
        for i in range(1,len(prices)):
            if prices[i]<minPrice:
                minPrice=prices[i]
            else:
                profit = prices[i]-minPrice
                maxP=max(maxP,profit)
        return maxP

        