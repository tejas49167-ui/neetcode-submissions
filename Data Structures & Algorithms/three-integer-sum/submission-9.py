class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort() 

        n = len(nums)

        l = [] 
        
        for i in range(n-2) : 

            j = i+1
            k = n-1 

            while j < k : 
                tem = nums[i]+nums[j]+nums[k]
                if tem==0 and [nums[i],nums[j],nums[k]] not in l  : 
                    l.append([nums[i],nums[j],nums[k]])
                    j+=1 
                    k-=1 
                elif tem < 0 : 
                    j+=1 
                else : 
                    k-=1 

        
        return l 
                