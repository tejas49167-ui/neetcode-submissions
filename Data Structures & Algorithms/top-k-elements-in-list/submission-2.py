class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums) 
        sc = sorted(c.items(),key=lambda x : x[1],reverse=True)

        ans = [] 
        for i in range(k) : 
            ans.append(sc[i][0]) 

        return ans 



        
        