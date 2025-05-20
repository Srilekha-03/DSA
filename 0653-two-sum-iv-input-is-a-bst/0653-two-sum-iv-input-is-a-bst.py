# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        nodes = []
        self.inOrderTraversal(root, nodes)
        i, j = 0, len(nodes) - 1
        while i < j:
            total = nodes[i].val + nodes[j].val
            if total == k:
                return True
            elif total < k:
                i += 1
            else:
                j -= 1
        return False
    def inOrderTraversal(self, root: TreeNode, nodes: list) -> None:
        if not root:
            return
        self.inOrderTraversal(root.left, nodes)
        nodes.append(root)
        self.inOrderTraversal(root.right, nodes)

        