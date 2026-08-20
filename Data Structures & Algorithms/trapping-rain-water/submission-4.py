class Solution:
    def trap(self, height: List[int]) -> int:

        n = len(height) 

        ml = [0,height[0]] 
        mr = [0,height[-1]] 


        for _ in range(1,n) : 
            ml.append(max(height[_],ml[-1]))
        
        for _ in range(n-2,-1,-1) : 
            mr.append(max(height[_],mr[-1]))
 
        mr[:] = mr[::-1]


        res = 0 

        for i in range(1,n) : 
            m_l = ml[i]
            m_r = mr[i]
        
            r =min(m_l,m_r) - height[i]
            if r>0 : 
                res +=r
                

        return res