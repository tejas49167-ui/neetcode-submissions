class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        i = 0 

        for w in t : 
            if i==len(s) : 
                return True 
            if w==s[i] : 
                i +=1 

        return i==len(s)
        