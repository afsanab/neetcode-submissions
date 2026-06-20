class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        else:
            max_p = 0
            l = 0
            r = 1
            while r < len(prices):
                profit = prices[r] - prices[l]
                if profit > max_p:
                    max_p = profit
                elif profit <=0:
                    l = r
                    r += 1
                else:
                    r +=1
        return max_p
                    