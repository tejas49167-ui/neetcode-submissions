class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(haystack) 
        m= len(needle) 
        i = 0 
        j = 0 
        while i<n : 
            curri = i 
            while j<m and i<n and haystack[i]==needle[j] : 
                i+=1 
                j+=1 

            if j==m : 
                return i-(m)
            else :
                j = 0 
                i = curri

            i+=1 
        return -1 
        