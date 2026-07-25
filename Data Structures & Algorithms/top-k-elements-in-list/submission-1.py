class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        l = [] 
        c = Counter(nums) 
        l = sorted(c,key=lambda i :c[i], reverse = True )
        return [l[i] for i in range(k)]
        