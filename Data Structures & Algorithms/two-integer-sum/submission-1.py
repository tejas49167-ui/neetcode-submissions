class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        d = {} 
        for i in range(n): 
            wanted = target - nums[i] 
            if wanted in d : 
                return [d[wanted],i] 
            d[nums[i]] = i 
        return [-1,-1]
        