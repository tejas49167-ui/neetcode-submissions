class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        s = set(nums) 
        original_list_len = len(nums)
        set_len = len(s) 

        if original_list_len == set_len : 
            return False     

        return True     

        