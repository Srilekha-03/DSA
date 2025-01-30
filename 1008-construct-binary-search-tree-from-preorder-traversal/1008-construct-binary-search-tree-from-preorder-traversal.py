# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        
        def build_tree(preorder, low, high):
            if not preorder or preorder[0] < low or preorder[0] > high:
                return None

            root_val = preorder.pop(0)
            root = TreeNode(root_val)

            root.left = build_tree(preorder, low, root_val)
            root.right = build_tree(preorder, root_val, high)

            return root

        return build_tree(preorder, float('-inf'), float('inf'))

        