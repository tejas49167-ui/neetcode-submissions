class Solution:
    def isPalindrome(self, s: str) -> bool:
       
        v = set('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789')
        sm = '' 
        l = 0 
        
        for i in s : 
            if i in v : 
                sm +=i.lower()
        r = len(sm) -1 
        while l <= r : 
            if sm[l]!=sm[r]: 
                return False 
            l +=1 
            r -=1 
        return True 
        