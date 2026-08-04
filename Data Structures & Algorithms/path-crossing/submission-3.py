class Solution:
    def isPathCrossing(self, path: str) -> bool:
        s = {(0,0)}

        x = 0 
        y = 0 

        for i in path : 
            if i=='N' : 
                x +=1 
            elif i=='S' : 
                x-=1 
            elif i=='E' : 
                y -=1 
            else : 
                y +=1 
            
            curr = (x,y)

            if curr in s : 
                return True 

            s.add(curr) 

        return False 

        