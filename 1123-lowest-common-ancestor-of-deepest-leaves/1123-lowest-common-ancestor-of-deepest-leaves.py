# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def lcaDeepestLeaves(self, root):
        def maxDepth(node):
            if not node:
                return 0
            return 1 + max(maxDepth(node.left), maxDepth(node.right))
        
        def dfs(node, maxi, length):
            if not node:
                return None
            if maxi - 1 == length:
                return node
            left = dfs(node.left, maxi, length + 1)
            right = dfs(node.right, maxi, length + 1)
            if left and right:
                return node
            return left if left else right
        
        maxi = maxDepth(root)  # maxi is the max depth
        return dfs(root, maxi, 0)