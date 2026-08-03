class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int] :
        
        c = Counter(nums) 

        sc = sorted(c,key = lambda x : c[x] , reverse=True) 


        return [sc[i] for i in range(k)]
        



        
        