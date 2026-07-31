class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        d = defaultdict(list) 
        for i in strs : 
            sori = "".join(sorted(i))
            
            d[sori].append(i)

      
        return [d[i] for i in d] 
            
            


        
        