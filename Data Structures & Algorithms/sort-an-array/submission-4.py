class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # hm = [0] * (max(nums)+1 )

        # for i in nums : 
        #     hm[i] +=1 

        # res = [] 

        # for i in range(len(hm)) : 
        #     for _ in range(hm[i]):
        #         res.append(i)
        # return res

        c = Counter(nums) 

        minn = min(nums) 
        maxx = max(nums) 
        j = 0 
        for i in range(minn,maxx+1) : 
            for _ in range(c[i]) : 
                nums[j] = i 
                j +=1 
        return nums