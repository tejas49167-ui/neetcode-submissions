class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:


        c = Counter(nums) 

        miss = 0 
        repeat = 0 
        for i in range(1,len(nums)+1) : 
            if c[i]==0 : 
                miss = i 

            elif c[i]==2 : 
                repeat = i 
            
        return [repeat,miss]
                   
        