class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i = 0 
        j = 0 

        m = len(haystack) 
        n = len(needle)
        while i<m : 
            curri = i 
            while i<m and j<n and haystack[i]==needle[j] : 
                i+=1 
                j+=1 

            if j==n : 
                return i-j
            
            j = 0 
            i =curri 
            i+=1 
        
        return -1 
            