class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        def p(s1,s2) : 
            r = ''
            for i in range(min(len(s1),len(s2))) : 
                if s1[i]==s2[i] : 
                    r +=s1[i] 
                else : 
                    break 
                

            return r 


        res = strs[0] 

        for i in range(1,len(strs)) : 
            res = p(strs[i],res)

        return res 
        