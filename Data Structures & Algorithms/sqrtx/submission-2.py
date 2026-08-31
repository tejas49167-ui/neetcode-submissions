class Solution:
    def mySqrt(self, x: int) -> int:

        l = 0 
        h = x 

        ans = 1

        while l <=h : 
            mid = (l+h) // 2 

            if mid * mid <= x : 
                ans = mid 
                l = mid + 1 
            
            else : 
                h = mid - 1 

        
        return ans 

        