class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        maj = len(nums) //2 

        c = Counter(nums) 

        for i in c : 
            if c[i]>=maj : 
                return i 

        