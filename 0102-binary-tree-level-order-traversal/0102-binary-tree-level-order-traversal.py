# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        res=[]
        q=[]
        q.append(root)
        while q:
            size=len(q)
            lis=[]
            for i in range(size):
                node=q.pop(0)
                lis.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(lis)
        return res
        
                

        
        