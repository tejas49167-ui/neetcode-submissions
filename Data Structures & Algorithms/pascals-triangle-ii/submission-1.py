class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ans = [[1]] 
        for i in range(1,rowIndex+1) : 
            st = [0] + ans[-1] 
            nd = ans[-1] + [0] 
            for j in range(i+1) : 
                st[j] +=nd[j] 
            ans.append(st) 
        return ans[rowIndex]
        