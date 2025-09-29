# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.paths=[]
        path=[]
        self.solve(root,path)
        lis_int=[int("".join(map(str, p))) for p in self.paths]
        return sum(lis_int)

    def solve(self,root,path):
        if not root:
            return 
        path.append(root.val)
        if not root.left and not root.right:
            self.paths.append(path[:])
        self.solve(root.left,path)
        self.solve(root.right,path)
        path.pop()
        