class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        left = 0
        right = 1
        profit = 0
        while right<len(prices):
            if prices[left]<prices[right]: 
                profit = max(profit, prices[right]-prices[left])
            else:
                left = right
            right += 1
        return profit
