class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        def startswith(sts , mst) : 
            i = 0 
             
            n = len(sts) 
            m = len(mst) 
            if m<n : 
                return False 
            while i<n : 
                if sts[i] != mst[i] : 
                    return False 
                i +=1 
            return True 
        p = strs[0] 
        for i in range(1,len(strs)) : 
            while not startswith(p,strs[i]) : 
                p = p[:-1]
        return p 


        