# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        n=len(preorder)
        self.ind=0
        post_index={val:i for i,val in enumerate(postorder)}
        def helper(start,end):
            if start>end :
                return None

            rootval=preorder[self.ind]
            i=post_index[rootval]
            root=TreeNode(rootval)
            self.ind+=1
            if start == end or self.ind >= n:
                return root
            leftval=preorder[self.ind]
            leftind=post_index[leftval]
    
            root.left=helper(start,leftind)
            root.right=helper(leftind+1,end-1)
            return root
        return helper(0,n-1)
        