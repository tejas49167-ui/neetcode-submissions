class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:

        m = -1 

        for i in range(len(s)) : 
            for j in range(i+1, len(s)) : 
                if s[i]==s[j] : 
                    m = max(abs(i-j)-1,m)

        return m 
                

        
        