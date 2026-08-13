class Solution:
    def maxScore(self, s: str) -> int:

        m = 0 

        for i in range(1,len(s)) : 

            cur = 0 

            for j in range(0,i) : 
                if s[j]=='0' : 
                    cur +=1 
            for j in range(i,len(s)): 
                if s[j]=='1' : 
                    cur +=1 
            
            m = max(m,cur) 

        
        return m

        