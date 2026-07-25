class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        l = [] 
        c = Counter(nums) 
        l = sorted(c,key=lambda x :c[x], reverse = True )
        return [l[i] for i in range(k)]
        