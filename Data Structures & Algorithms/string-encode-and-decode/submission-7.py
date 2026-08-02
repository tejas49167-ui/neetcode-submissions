class Solution:

    def encode(self, strs: List[str]) -> str:
        es ="" 
        for i in strs : 
            es +=str(len(i))
            es +='#'
            es +=i
            
        return es 

        

    def decode(self, s: str) -> List[str]:
        o_l  =[] 
     
        
        i = 0 
        while i<len(s) : 
            length =""
            while s[i]!='#' : 
                length +=s[i]
                i+=1
            i+=1 
            length = i+int(length) 

            t = ""
            while i<length : 
                t +=s[i]
                i +=1 
            o_l.append(t)
        return o_l


        
    
        
            
