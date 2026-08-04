class Solution:

    def encode(self, strs: List[str]) -> str:
        s = "" 
        for i in strs : 
            s +=str(len(i)) 
            s +='#' 
            s +=i 

        return s 
        

        

    def decode(self, s: str) -> List[str]:
        l = [] 
        i = 0 
        while i < len(s): 

            n = '' 
            while s[i] != '#' : 
                n +=s[i]
                i+=1  
            n = int(n) 
            i+=1 

            temp = '' 
            reach = i+n 
            while i<reach: 
                temp +=s[i]
                i+=1 

            l.append(temp)

             

        return l 
        


        
    
        
            
