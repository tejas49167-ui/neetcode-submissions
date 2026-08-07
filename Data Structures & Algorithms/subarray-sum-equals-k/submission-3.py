class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:


        count = 0 

        d = defaultdict(int)

        prefix = 0 
        d[prefix] = 1 

        for i in nums : 
            prefix +=i 
           
            count +=d[prefix-k]
            
            d[prefix] +=1 
          

        return count 

