# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        n=len(postorder)
        self.index=n-1

        def solve(start,end):
            if start>end:
                return None
            rootval=postorder[self.index]
            i=start
            for ind in range(start,end+1):
                if inorder[ind]==rootval:
                    i=ind
                    break
            self.index-=1
            root=TreeNode(rootval)
            root.right=solve(i+1,end)
            root.left=solve(start,i-1)
            return root
        return solve(0,n-1)

        