# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        result=[]
        self.recursion(root,result,0)
        return result
    def recursion(self,root,result,level):
        if root is None:
            return
        if level==len(result):
            result.append(root.val)
        if root.right:
            self.recursion(root.right,result,level+1)
        if root.left:
            self.recursion(root.left,result,level+1)