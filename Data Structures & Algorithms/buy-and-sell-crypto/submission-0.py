class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minb = float("inf") 
        maxs = 0 

        for i in prices : 
            minb = min(minb, i)
            maxs = max(maxs,i-minb)
        return maxs
        