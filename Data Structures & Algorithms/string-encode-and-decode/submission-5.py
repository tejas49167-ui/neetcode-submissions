class Solution:

    def encode(self, strs: List[str]) -> str:
        es ="" 
        for i in strs : 
            es +=i
            es +='~'
        return es 

        

    def decode(self, s: str) -> List[str]:
        o_l  =[] 
     
        t = ""
        for i in range(len(s)) : 
            if s[i]=='~' :
                o_l.append(t)
                t = "" 
            else : 
                t +=s[i] 
        
        return o_l


        
    
        
            
