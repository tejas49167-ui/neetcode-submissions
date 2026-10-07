class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        c = Counter(nums) 

        j = 0 

        for _ in [0,1,2] : 
            for i in range(c[_]) : 
                nums[j]=_ 
                j+=1 
            
