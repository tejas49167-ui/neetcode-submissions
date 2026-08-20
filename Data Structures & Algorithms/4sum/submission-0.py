class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        nums.sort() 


        n = len(nums)

        l = []  

        for a in range(n-3) : 

            for b in range(a+1,n-2) : 

                c = b+1 
                d = n-1 

                while c < d : 

                    t = nums[a] + nums[b] + nums[c] + nums[d] 

                    if t==target and [nums[a],nums[b],nums[c],nums[d]] not in l  : 
                        l.append([nums[a],nums[b],nums[c],nums[d]])
                        c+=1 
                        d-=1
                    elif t < target : 
                        c +=1 
                    else : 
                        d -=1 

        return l 