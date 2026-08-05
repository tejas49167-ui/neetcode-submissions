class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums : 
            return 0 

        sn = set(nums) 
        
        longest=1
        m = 1
        for i in sn : 
            if i-1 not in sn : 
                longest =1 
                while i+longest in sn : 
                    longest +=1 

                m = max(longest,m) 

        return m 

        