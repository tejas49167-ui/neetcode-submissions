class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sd = Counter(s) 
        td = Counter(t) 

        for i in sd : 
            if sd[i] !=td[i]  : 
                return False 
        for i in td : 
            if td[i] != sd[i] : 
                return False 
        return True  