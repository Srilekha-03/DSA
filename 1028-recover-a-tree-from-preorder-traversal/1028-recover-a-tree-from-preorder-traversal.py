# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        # def level_order(root):
        #     q=[]
        #     ans=[]
        #     q.append(root)
        #     while q:
        #         node=q.pop(0)
        #         ans.append(node)
        #         if not node:
        #             if not node.left and not node.right:
        #                 continue
        #             q.append(node.left)
        #             q.append(node.right)               
        #     return ans
        dashes=0
        stack=[]
        i=0
        while i<len(traversal):
            if traversal[i]=='-':
                i+=1
                dashes+=1
            else:
                j=i
                while j<len(traversal) and traversal[j]!='-':
                    j+=1
                value=int(traversal[i:j])
                node=TreeNode(value)
                while len(stack)>dashes:
                    stack.pop()
                if stack and stack[-1].left is None:
                    stack[-1].left=node
                elif stack:
                    stack[-1].right=node
                stack.append(node)
                i=j
                dashes=0
        root=stack[0]
        return root
        
        
        