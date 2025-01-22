# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxi = float('-inf')
        def leftRightSum(root):
            nonlocal maxi #using a non local var
            if root is None:
                return 0
            left=max(0,leftRightSum(root.left))
            right=max(0,leftRightSum(root.right))
            maxi=max(maxi,left+right+root.val)
            return root.val+max(left,right)
        leftRightSum(root)
        return maxi
        