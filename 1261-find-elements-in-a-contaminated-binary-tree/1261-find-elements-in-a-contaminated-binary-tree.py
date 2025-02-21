# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:
    def __init__(self, root):
        self.values = set()
        self.recover(root, 0)

    def recover(self, node, val):
        if not node:
            return
        node.val = val
        self.values.add(val)
        self.recover(node.left, 2 * val + 1)
        self.recover(node.right, 2 * val + 2)

    def find(self, target):
        return target in self.values
# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)