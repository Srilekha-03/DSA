# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root :
            return []

        def dfs(root,ind,ans):
            if not root:
                return 
            if len(ans)==ind:
                ans.append(root.val)
            else:
                ans[ind]=root.val
            dfs(root.left,ind+1,ans)
            dfs(root.right,ind+1,ans)   
        ans=[]
        dfs(root,0,ans) 
        return ans


        
        