class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        seen = set() 

        l = 0 

        for i in nums : 
            if i in seen : 
                return True 
            seen.add(i) 
            if len(seen) > k : 
                seen.remove(nums[l]) 
                l+=1 

        return False 