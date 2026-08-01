class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        l = [] 
        c = Counter(arr1) 
        for i in arr2 : 
            if i in c : 
                for j in range(c[i]) : 
                    l.append(i)
        tl = [] 
        for i in arr1 : 
            if i not in arr2 and i not in tl : 
                for j in range(c[i]) : 
                    tl.append(i)
        tl.sort() 
        l.extend(tl)
        return l 
        