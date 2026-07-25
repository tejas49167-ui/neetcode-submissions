class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        r = len(nums) 
        inc = 0 
        for i in range(r+1) : 
            if inc not in nums  :
                return inc 
            inc +=1 
        