class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        


        pt = [[1]] 

        for i in range(rowIndex) : 

            st = pt[-1] + [0] 
            nd = [0] + pt[-1]

            for j in range(len(st)) : 
                st[j] +=nd[j] 

            
            pt.append(st) 

        return pt[rowIndex]

            
