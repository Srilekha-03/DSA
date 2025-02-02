# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        q=deque()
        q.append((root,0))
        ans=0
        while q:
            size=len(q)
            mmin=q[0][1]
            last=0
            first=0
            for i in range(0,size):
                node,cur=q.popleft()
                cur=cur-mmin
                if i==0:
                    first=cur
                if i==size-1:
                    last=cur
                if node.left:
                    q.append((node.left,2*cur+1))
                if node.right:
                    q.append((node.right,2*cur+2))
            ans=max(ans,last-first+1)
        return ans


        