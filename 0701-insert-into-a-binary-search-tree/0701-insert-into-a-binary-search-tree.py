# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return TreeNode(val)
        cur=root
        while True:
            if cur.val<=val:
                if cur.right!=None:
                    cur=cur.right
                else:
                    cur.right=TreeNode(val)
                    break
            else:
                if cur.left!=None:
                    cur=cur.left
                else:
                    cur.left=TreeNode(val)
                    break
        return root

        