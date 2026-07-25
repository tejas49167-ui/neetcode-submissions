class Solution:

    def encode(self, strs: List[str]) -> str:
        en = ""
        for i in strs : 
            en +=(str(len(i))+'#'+i) 
        return en 

    def decode(self, s: str) -> List[str]:
        de =[] 
        i = 0 
        while i<len(s) : 
            j = i 
            while s[j]!='#' : 
                j+=1 
            
            length = int(s[i:j]) 

            text = s[j+1:j+length+1] 

            de.append(text) 

            i = j+1+length 
        return de 
    
    
        
            
