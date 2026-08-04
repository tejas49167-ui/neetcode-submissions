class Solution:
    def isPathCrossing(self, path: str) -> bool:
        s = [[0,0]]

        st = 0 
        nd = 0 

        for i in path : 
            if i=='N' : 
                st +=1 
            elif i=='S' : 
                st -=1 
            elif i=='E' : 
                nd -=1 
            else : 
                nd +=1 
            
            curr = [st,nd]

            if curr in s : 
                return True 

            s.append(curr) 

        return False 

        