class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        def p(s1,s2) : 
            r = ''
            i = 0
            while i<len(s1) and i<len(s2) and s1[i]==s2[i] : 
                r +=s1[i] 
                i+=1
            
            return r 


        res = strs[0] 

        for i in range(1,len(strs)) : 
            res = p(strs[i],res)

        return res 
        