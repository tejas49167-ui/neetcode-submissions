# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = [] 
        def pos(r):
            if not r : 
                return 
            
            pos(r.left) 
            pos(r.right) 
            ans.append(r.val) 
        pos(root)
        return ans                 



        