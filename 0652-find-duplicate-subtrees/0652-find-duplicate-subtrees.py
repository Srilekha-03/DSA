# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        se=dict()
        res=[]

        def solve(root):
            if not root:
                s=""
                s+="N"
                return s
            s=""
            s+=str(root.val)+','+solve(root.left)+','+solve(root.right)
            if s not in se:
                se[s]=1
            elif se[s]==1:
                res.append(root)
                se[s]+=1
            return s 

        solve(root)
        return list(res)
        