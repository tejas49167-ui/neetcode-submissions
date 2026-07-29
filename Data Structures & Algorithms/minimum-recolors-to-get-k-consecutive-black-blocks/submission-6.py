class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        arr = blocks.split('W')
        for i in arr : 
            if len(i)>=k : 
                return 0 

        ans = 101
        wcoloring = 0 
        for i in range(len(blocks)-k+1): 
            wcoloring = 0 
            for j in range(i,i+k) : 
                if blocks[j]=='W' : 
                    wcoloring +=1 
            ans = min(ans,wcoloring)
            
        
        return min(wcoloring,ans)
        
        
        