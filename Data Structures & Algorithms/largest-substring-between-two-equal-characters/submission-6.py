class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:

        m = -1 
        first = {} 
        for i in range(len(s)) : 
            if s[i] not in first : 
                first[s[i]] = i 
            else :
                m = max(i-first[s[i]]-1,m)

        return m 
                

        
        