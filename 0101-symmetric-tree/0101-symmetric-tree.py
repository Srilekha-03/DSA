# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.solve(root.left,root.right)
    def solve(self,left,right):
        if not left or not right:
            return left==right
        if left.val!=right.val:
            return False
        return self.solve(left.left,right.right) and self.solve(left.right,right.left)

        