class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0 
        minb = 101 

        for i in prices : 
            minb = min(i,minb)
            profit = max(profit,i-minb)

        return profit 
