# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        t1 = headA 
      
        while t1 : 
            # every time 
            t2 = headB 
            while t2 : 
                if t1==t2 : 
                    return t1
                    
                t2 = t2.next 
            t1=t1.next 
            
        
        return None 
        