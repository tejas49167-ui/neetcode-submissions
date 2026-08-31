class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        m = 0 
        dd = defaultdict(int)
        left =  0 
        mcf = 0 
        for right in range(len(s)) : 
            dd[s[right]] +=1 
            mcf = max(mcf,dd[s[right]])
            
            while (right - left )+ 1 -mcf > k : 
                dd[s[left]] -=1 
                left +=1 

            m = max((((right-left) + 1 )) , m )

        return m 
        