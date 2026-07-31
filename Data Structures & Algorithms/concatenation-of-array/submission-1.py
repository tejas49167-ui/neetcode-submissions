class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        newnums = [0] * (n*2) 
        for i in range(len(nums)) : 
            newnums[i]=nums[i] 
            newnums[n+i] = nums[i]
        return newnums
        