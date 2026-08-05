class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # prefix = [1]

        # for i in nums : 
        #     prefix.append(prefix[-1]*i)

        # sufix = [1] 

        # for i in nums[::-1] : 
        #     sufix.append(sufix[-1]*i) 

        # ans = [] 

        # for i in range(len(suffix)) : 
        #     ans.append(prefix[i]*)

        ans = [1] * len(nums) 

        pre = 1 
        for prefix in range(len(nums)) : 
            ans[prefix] = pre 
            pre *=nums[prefix]

        suf = 1

        for suffic in range(len(nums)-1,-1,-1) : 
            ans[suffic] *=suf 
            suf *=nums[suffic]

        
        return ans 







        


        