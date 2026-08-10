class Solution:

    def generate(self, numRows: int) -> List[List[int]]:

        res = [[1]] 


        for i in range(numRows-1) : 
            st = [0] + res[-1] 

            sn = res[-1] + [0] 


            for j in range(len(st)) : 
                st[j] +=sn[j]

            res.append(st) 

        return res  


        