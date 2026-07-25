class Solution:
    def maxDifference(self, s: str) -> int:
        c = Counter(s) 
        o = [] 
        e = [] 
        for i in c : 
            if c[i]%2==0 : 
                e.append(c[i]) 
            else : 
                o.append(c[i]) 
        return max(o) - min(e)
        