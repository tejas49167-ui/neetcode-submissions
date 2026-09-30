class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        d = defaultdict(list) 

        for i in strs : 
            temp = ''.join(sorted(i))  

            d[temp].append(i) 


        return [d[l] for l in d]
        
        
 

        


        
        