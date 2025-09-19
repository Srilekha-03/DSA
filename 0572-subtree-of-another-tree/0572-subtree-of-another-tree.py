# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None:
            return False

        if root.val==subRoot.val:
            if self.isIdentical(root,subRoot):
                return True

        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)

    def isIdentical(self,p,q):
        if not p or not q:
            return p==q
        if p.val!=q.val:
            return False
        return self.isIdentical(p.left,q.left) and self.isIdentical(p.right,q.right)

            

        