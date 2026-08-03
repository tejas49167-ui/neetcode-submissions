class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        c = Counter(nums) 

        j = 0 

        for i in range(3) : 
            if i in c : 
                for _ in range(c[i]) : 
                    nums[j] = i 
                    j +=1 
        
