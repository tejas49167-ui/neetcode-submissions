class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        sn = set(nums) 

        for i in range(1,len(nums)+100) : 
            if i not in sn : 
                return i 


        