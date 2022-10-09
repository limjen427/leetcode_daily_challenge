# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        res = self.inorderTraversal(root)
        
        
        for i in range(1, len(res)):
            if (res[i] <= res[i-1]):
                return False
        return True
        #return root.val > self.isValidBST(root.left) and root.val < self.isValidBST(root.right)
    
    
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if root:
            res += self.inorderTraversal(root.left)
            res.append(root.val)
            res += self.inorderTraversal(root.right)
        return res