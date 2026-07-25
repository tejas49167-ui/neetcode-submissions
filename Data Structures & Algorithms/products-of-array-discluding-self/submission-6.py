class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res =[] 
        X  = 1 
        length = len(nums)
        zero_presence = 0  
        for i in range(length) :
            if nums[i]==0 : 
                zero_presence +=1 
            else : 
                X *= nums[i] 


        if zero_presence > 1 : 
            return [0] * length

        for i in range(len(nums)) : 
            if nums[i]==0 : 
                res.append(X) 
            elif zero_presence == 1 : 
                res.append(0)
            else : 
                res.append(X//nums[i])
                 
        return res 
        