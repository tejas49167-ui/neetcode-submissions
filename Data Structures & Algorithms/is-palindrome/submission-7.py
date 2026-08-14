class Solution:
    def isPalindrome(self, s: str) -> bool:
        sm = '' 
        l = 0 
        for i in s : 
            if (ord(i)>=ord('a') and ord(i)<=ord('z')) or (ord(i)>=ord('A') and ord(i)<=ord('Z')) or (ord(i)>=ord('0') and ord(i)<=ord('9')) : 
                sm +=i.lower()
        return sm==sm[::-1]