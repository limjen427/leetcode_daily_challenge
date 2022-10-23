# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #BFS
        # for loop 끝나고 queue에 있는 모든것들을 res.append(cur)
        res = []
        
        if not root:
            return []
        
        queue = [root]
        
        while queue:
            cur = []
            ql = len(queue)
            for i in range(ql):
                node = queue.pop(0)
                cur.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                
            res.append(cur)
        return res