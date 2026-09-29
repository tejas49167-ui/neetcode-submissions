class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        def pre(q,w) : 
            r = ''
            for _ in range(min(len(q),len(w))) : 
                if q[_]==w[_] : 
                    r +=q[_] 
                else : 
                    break 

            return r 
            

        res = strs[0]
        for i in strs : 
            res = pre(res,i)

        return res 

        