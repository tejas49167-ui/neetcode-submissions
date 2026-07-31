class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums) 
        d = defaultdict(int)
        for i in nums : 
            d[i] +=1 
            if d[i] > n//2 : 
                return i 
        return -1 
