# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        summ=0
        def helper(root):
            nonlocal summ
            if root is None:
                return 0
            leftsum=helper(root.left)
            rightsum=helper(root.right)
            summ+=abs(leftsum-rightsum)
            return root.val+leftsum+rightsum

        helper(root)
        return summ

        