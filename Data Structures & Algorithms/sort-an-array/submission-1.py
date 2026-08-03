class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        c = Counter(nums)

        k1 = min(nums) 
        k2 = max(nums)

        j = 0 
        for i in range(k1,k2+1) : 
            if i in c : 
                for _ in range(c[i]) : 
                    nums[j] = i 
                    j +=1 
        return nums 
            