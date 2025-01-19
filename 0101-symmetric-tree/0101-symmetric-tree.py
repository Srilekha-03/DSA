# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return root==None or self.symmetric(root.left,root.right)
    def symmetric(self,left,right):
        if left==None or right==None:
            return left==right
        if left.val!=right.val:
            return False
        return self.symmetric(left.left,right.right) and self.symmetric(left.right,right.left)