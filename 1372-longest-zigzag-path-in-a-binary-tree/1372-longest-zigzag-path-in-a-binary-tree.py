# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans=0
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        l=self.helper(root.left,0)
        r=self.helper(root.right,1)
        self.ans=max(self.ans,l,r)
        return self.ans
    def helper(self,root,val):
        if not root:
            return 0
        l=self.helper(root.left,0)
        r=self.helper(root.right,1)
        self.ans=max(lh,rh)
        if val==0:
            return self.helper(root.right,1)
        else

        