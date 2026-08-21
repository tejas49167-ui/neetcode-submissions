class Solution:
    def trap(self, height: List[int]) -> int:

        n = len(height) 

        # ml = [height[0]] 
        # mr = [height[-1]] 


        # for _ in range(1,n) : 
        #     ml.append(max(height[_],ml[-1]))
        
        # for _ in range(n-2,-1,-1) : 
        #     mr.append(max(height[_],mr[-1]))
 
        # mr[:] = mr[::-1]


        # res = 0 

        # for i in range(1,n) : 
        #     m_l = ml[i]
        #     m_r = mr[i]
        
        #     res+=min(m_l,m_r) - height[i]


        i = 0 
        j = n -1 
        ml,mr = 0,0 
        res = 0 
        while i < j : 
            if height[i] < height[j]: 
                if height[i] > ml : 
                    ml = height[i]
                else : 
                    res +=ml-height[i] 
                i+=1  
            else : 
                if height[j] > mr : 
                    mr = height[j]
                else : 
                    res +=mr-height[j] 
                j-=1 
         
                

        return res