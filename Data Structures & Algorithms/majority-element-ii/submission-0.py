class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        c = Counter(nums)

        ms = len(nums)//3 

        return [i for i in c  if c[i] > ms ]
