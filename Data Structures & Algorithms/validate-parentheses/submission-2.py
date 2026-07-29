class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] 
        d = {')' : '(' , '}' : '{' , ']' : '['}
        if len(s) %2 !=0 : 
            return False 
        for i in s : 
            if i in d.values(): 
                stack.append(i) 
            else : 
                if not stack or stack.pop() != d[i] : 
                    return False 
        return len(stack)==0 
        