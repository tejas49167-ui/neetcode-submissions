class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        ps = {} 

        slist = s.split() 

        if len(slist) !=len(pattern) : 
            return False 

        sp = {} 

        for i in range(len(pattern)) : 
            if pattern[i] in ps : 
                if ps[pattern[i]] != slist[i] : 
                    return False 
            else : 
                ps[pattern[i]] = slist[i] 

  

            if slist[i] in sp : 
                if sp[slist[i]] != pattern[i] : 
                    return False 
            else : 
                sp[slist[i]] = pattern[i]


        return True 
        