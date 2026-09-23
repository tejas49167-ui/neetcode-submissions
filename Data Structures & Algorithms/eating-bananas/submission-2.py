class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        l = 1 
        r = max(piles)
        


        curr = 0 
        while l<=r : 
            i = (l+r) // 2 

    
            for j in piles : 
                curr +=math.ceil(j/i) 

            if curr<=h : 
                r = i - 1 
            else : 
                l = i+1 
            curr = 0 
        return l 



