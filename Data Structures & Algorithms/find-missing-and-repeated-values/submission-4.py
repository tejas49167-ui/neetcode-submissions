class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        arr = [] 
        for i in grid : 
            for j in i :
                arr.append(j)

        ans = [] 
        for i in arr : 
            if arr.count(i)==2 : 
                ans.append(i) 
                break 
        
        
        for i in range(1,len(arr)+1) : 
            if i not in arr : 
                ans.append(i) 
                return ans 
