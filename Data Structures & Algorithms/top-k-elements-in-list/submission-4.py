class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int] :
        
        c = Counter(nums) 

        cs = sorted(c,key=lambda i : c[i],reverse=True) 

        return [cs[i] for i in range(k)]

        
        