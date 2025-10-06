# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxi=float('-inf')
        self.solve(root)
        return self.maxi
    def solve(self,root):
        if not root:
            return 0
        l=self.solve(root.left)
        r=self.solve(root.right)
        path_v=l+r+root.val
        only_root=root.val
        max_l_r=max(l,r)+root.val
        self.maxi=max(self.maxi,path_v,only_root,max_l_r)
        return max(only_root,max_l_r)