# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        if root is None:
            return []
        parent=self.parentMap(root)
        q=deque()
        visited=set()
        q.append(target)
        visited.add(target)
        cur_level=0
        while q:
            if cur_level==k:
                break
            cur_level+=1
            size=len(q)
            for i in range(0,size):
                node=q.popleft()
                if node.left and node.left not in visited:
                    visited.add(node.left)
                    q.append(node.left)
                if node.right and node.right not in visited:
                    visited.add(node.right)
                    q.append(node.right)
                if node in parent and parent[node] and parent[node] not in visited:
                    visited.add(parent[node])
                    q.append(parent[node])
        return [node.val for node in q]

    def parentMap(self,root):
        d = {root: None} 
        q=deque()
        q.append(root)
        while q:
            node=q.popleft()
            if node.left:
                d[node.left]=node
                q.append(node.left)
            if node.right:
                d[node.right]=node
                q.append(node.right)
        return d
        
        