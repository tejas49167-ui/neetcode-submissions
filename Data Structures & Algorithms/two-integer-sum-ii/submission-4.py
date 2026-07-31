class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        d =  {} 
        for i in range(len(numbers)): 
            t = target - numbers[i] 
            if t in d : 
                return [d[t]+1,i+1] 
            else : 
                d[numbers[i]] = i
        