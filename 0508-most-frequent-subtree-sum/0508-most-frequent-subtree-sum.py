# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        res=[]
        hashmap=defaultdict(int)

        def helper(root):
            if root is None:
                return 0
            summ=root.val+helper(root.left)+helper(root.right)
            hashmap[summ]+=1
            return summ
        

        helper(root)
        maxi=float("-inf")
        for value in hashmap.values():
            if value>maxi:
                maxi=value
        for key,value in hashmap.items():
            if value==maxi:
                res.append(key)
        return res
        
        