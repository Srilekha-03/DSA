# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        lh=self.minDepth(root.left)
        rh=self.minDepth(root.right)
        if lh==0:
            return 1+rh
        if rh==0:
            return 1+rh
        return 1+ min(lh,rh)
        