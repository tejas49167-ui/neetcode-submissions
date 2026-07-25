class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums : 
            return 0 
        s = set(nums) 
        l = sorted(s) 

        res = 0 
        curr = 1
        for i in range(len(l)-1) : 
            if l[i]+1==l[i+1] : 
                curr +=1 
            else : 
                res = max(res,curr) 
                curr = 1 
        return max(res,curr) 
