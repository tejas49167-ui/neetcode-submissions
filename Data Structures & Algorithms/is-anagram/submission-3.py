class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ds = {}  
        dt = {}  
        for letters in s  :
            if letters in ds: 
                ds[letters] +=1   
            else : 
                ds[letters] = 1 
        
        for letters in t  :
            if letters in dt: 
                dt[letters] +=1 
            else : 
                dt[letters] = 1 

        
        return ds==dt  
        



            
        
        