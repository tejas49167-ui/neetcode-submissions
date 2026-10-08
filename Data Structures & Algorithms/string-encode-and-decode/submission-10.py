class Solution:

    def encode(self, strs: List[str]) -> str:
        res = '' 
        for i in strs : 
            res +=i 
            res +='`'
        return res 

    def decode(self, s: str) -> List[str]:
        return s.split('`')[:-1]

        


        
    
        
            
