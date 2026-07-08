class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        cheapest = prices[0]
        for item in prices:
            if item < cheapest:
                cheapest = item
            else:
                profit = max(profit,item-cheapest)
        return profit
            