class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # buy the lowest sell the highest
        # start at index 0 and iterate
        # if the value later is smaller than current, move pointer
        # store the maximum sell value

        sell, profit = 0, 0
        l = prices[0]
        for r in range(1, len(prices)):
            if prices[r] < l:
                l = prices[r]
            else:
                profit = prices[r] - l

            sell = max(profit, sell)
        return sell