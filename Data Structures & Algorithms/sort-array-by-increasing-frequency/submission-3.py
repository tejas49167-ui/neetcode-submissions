class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        
        c = Counter(nums) 

        sc = sorted(c,key = lambda x : (c[x],-x)) 

        return [i for i in sc for j in range(c[i]) ]