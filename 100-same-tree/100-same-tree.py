# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if (not p) and (not q): 
            return True
        if (not p and q) or (p and not q): 
            return False
        if p.val != q.val: 
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
    
    
    
    
    
#         porder = self.inorder(p)
#         print("--------")
#         qorder = self.inorder(q)
        
#         return porder == qorder
            
    
#     def inorder(self, root: Optional[TreeNode]) -> List[int]:
#         res = []
#         if root:
#             res += self.inorder(root.left)
#             if root.val == None:
#                 res.append(None)
#                 print("null", end = ' ')
#             else:
#                 res.append(root.val)
#                 print(root.val, end = ' ')
#             res += self.inorder(root.right)
#         return res