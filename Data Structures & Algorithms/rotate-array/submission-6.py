class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        n  = len(nums)
        k %=n

        def rev(l=0,r=n-1) : 
            while l<r : 
                nums[l],nums[r] = nums[r] , nums[l]
                l+=1 
                r -=1 

        rev()
        rev(0,k-1) 
        rev(k)


               
