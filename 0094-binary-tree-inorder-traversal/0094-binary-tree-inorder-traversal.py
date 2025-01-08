# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = []

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root==None:
            return []
        stack=[]
        node=root
        while True:
            if node!=None:
                stack.append(node)
                node=node.left
            else:
                if not stack:
                    break
                node=stack.pop()
                self.ans.append(node.val)
                node=node.right
        return self.ans
        