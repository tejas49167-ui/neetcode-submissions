class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        ones = [] 
        for i in range(len(boxes)) : 
            if boxes[i]=='1' : 
                ones.append(i)
        l = [] 
        for i in range(len(boxes)) : 
            an = 0 
            for j in ones : 
                an +=abs(i-j)
            l.append(an)
        return l 





        