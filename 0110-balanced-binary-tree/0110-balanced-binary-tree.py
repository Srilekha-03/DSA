# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        def height(root):
            if root is None:
                return 0
            return 1 + max(height(root.left),height(root.right))

        leftH=height(root.left)
        rightH=height(root.right)
        if abs(leftH-rightH)>=2:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)
        
        
        