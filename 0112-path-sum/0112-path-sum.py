# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        def helper(root,summ):
            if not root:
                return False
            summ+=root.val
            if not root.left and not root.right:
                if summ==targetSum:
                    return True
                else:
                    return False
            if helper(root.left,summ):
                return True
            if helper(root.right,summ):
                return True
            return False

        return helper(root,0)
        