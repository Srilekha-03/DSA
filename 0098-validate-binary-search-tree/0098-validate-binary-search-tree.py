# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.bst(root,float('-inf'),float('inf'))
    def bst(self,root,mini,maxi):
        if root is None:
            return True
        if root.val>=maxi or root.val<=mini:
            return False
        return self.bst(root.left,mini,root.val) and self.bst(root.right,root.val,maxi)
        