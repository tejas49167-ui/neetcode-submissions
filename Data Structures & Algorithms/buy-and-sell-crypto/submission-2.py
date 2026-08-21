class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0 
        buy = 1000000
        for i in prices : 
            if i < buy : 
                buy = i
            else  :
                profit = max(profit,i-buy)

        return profit