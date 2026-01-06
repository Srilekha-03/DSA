# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from math import inf
from collections import deque
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        q=deque()
        q.append(root)
        level=1
        maxi=-inf
        ans=1
        while q:
            n=len(q)
            maxv=0
            for i in range(n):
                node=q.popleft()
                maxv+=node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if maxv>maxi:
                maxi=maxv
                ans=level
            level+=1
        return ans
        


        