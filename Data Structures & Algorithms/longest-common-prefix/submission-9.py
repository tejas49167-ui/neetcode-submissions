class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        st = strs[0] 
 
        for i in strs[1:] : 

            j = 0 
            while j < len(st) and j < len(i) and st[j]==i[j] : 
                j+=1

            st = st[:j] 
            

        return st



      