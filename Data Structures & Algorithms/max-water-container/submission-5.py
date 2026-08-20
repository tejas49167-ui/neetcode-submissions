class Solution:
    def maxArea(self, heights: List[int]) -> int:
        m = 0

        n = len(heights) 

        i = 0 
        j = n - 1 

        while i < j : 

            if heights[i] < heights[j] : 
                area = heights[i] * (j - i)
                i+=1 
            else  :
                area = heights[j] * (j - i )
                j-=1 

            m = max(m,area) 


        
        return m 
