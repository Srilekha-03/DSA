# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteHelper(self, root, st, result):
        if not root:
            return None
        root.left = self.deleteHelper(root.left, st, result)
        root.right = self.deleteHelper(root.right, st, result)
        if root.val in st:
            if root.left:
                result.append(root.left)
            if root.right:
                result.append(root.right)
            return None
        return root

    def delNodes(self, root, to_delete):
        result = []
        st = set(to_delete)
        self.deleteHelper(root, st, result)
        if root and root.val not in st:
            result.append(root)
        return result