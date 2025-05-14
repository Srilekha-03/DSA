# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root):
        nodes = []
        self.preorder(root, nodes)
        n = len(nodes)
        for i in range(1, n):
            prev = nodes[i - 1]
            prev.left = None
            prev.right = nodes[i]
    def preorder(self, root, nodes):
        if not root:
            return
        nodes.append(root)
        self.preorder(root.left, nodes)
        self.preorder(root.right, nodes)