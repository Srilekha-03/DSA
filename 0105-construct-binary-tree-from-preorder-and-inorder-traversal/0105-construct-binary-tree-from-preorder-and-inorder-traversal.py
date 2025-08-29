# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        n=len(preorder)
        self.pre_index = 0

        def solve(start,end):
            if start>end:
                return None
            rootval=preorder[self.pre_index]
            i=start
            for ind in range(start,end+1):
                if inorder[ind]==rootval:
                    i=ind
                    break
            self.pre_index += 1
            root=TreeNode(rootval)
            root.left=solve(start,i-1)
            root.right=solve(i+1,end)
            return root


        return solve(0,n-1)
        