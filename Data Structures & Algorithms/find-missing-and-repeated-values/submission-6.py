class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:

        l = [] 

        for i in grid : 
            for j in i : 
                l.append(j) 


        ans = [] 

        c = Counter(l)

        for i in l : 
            if c[i]==2 : 
                ans.append(i) 
                break 
        sl = set(l)
        for i in range(1,len(l)+1) : 
            if i not in sl : 
                ans.append(i) 
                break 

        return ans 
        