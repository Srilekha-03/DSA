# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return root
        if root.val==key:
            return self.deletion(root)
        dummy=root
        while root:
            if root.val>key:
                if root.left and root.left.val==key:
                    root.left=self.deletion(root.left)
                else:
                    root=root.left
            else:
                if root.right and root.right.val==key:
                    root.right=self.deletion(root.right)
                else:
                    root=root.right
        return dummy
    def deletion(self,root):
        if not root.left:
            return root.right
        if not root.right:
            return root.left
        rightChild=root.right
        lastRightFromLeft=self.lastRight(root.left)
        lastRightFromLeft.right=rightChild
        return root.left
    def lastRight(self,root):
        if root.right is None:
            return root 
        return self.lastRight(root.right)


                
                
        