class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:

        curr_max = nums[0] 

        m = nums[0]

        for i in range(len(nums)-1) : 
            if nums[i] < nums[i+1] : 
                curr_max +=nums[i+1] 

            else : 
                m = max(curr_max,m) 
                curr_max = nums[i+1] 

        return max(curr_max,m) 
