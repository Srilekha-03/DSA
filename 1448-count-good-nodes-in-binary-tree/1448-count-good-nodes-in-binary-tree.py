# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.count = 0
    def goodNodes(self, root: TreeNode) -> int:
        self.helper(root,root.val)
        return self.count
    def helper(self,root,maxi):
        if not root:
            return 
        if root.val>=maxi:
            self.count+=1
            self.helper(root.left,root.val)
            self.helper(root.right,root.val)
            return
        self.helper(root.left,maxi)
        self.helper(root.right,maxi)
    




        