# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        q=[]
        result=[]
        flag=True
        q.append(root)
        while q:
            n=len(q)
            row=[0]*n
            for i in range(n):
                node=q[0]
                del q[0]
                index = i if flag else n-i-1
                row[index]=node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            flag=not flag
            result.append(row)
        return result


        