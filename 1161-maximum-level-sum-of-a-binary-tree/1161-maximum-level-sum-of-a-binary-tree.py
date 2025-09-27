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
        ans=dict()
        q=deque()
        q.append(root)
        level=1
        while q:
            temp=[]
            n=len(q)
            for i in range(n):
                node=q.popleft()
                temp.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ans[level]=temp
            level+=1
        for key,val in ans.items():
            ans[key]=sum(val)
            
        maxi=-inf
        maxl=-1
        for key,val in ans.items():
            if val>maxi:
                maxi=val
                maxl=key
        return maxl


        