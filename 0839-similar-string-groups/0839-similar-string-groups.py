from collections import defaultdict
class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        adj=defaultdict(list)
        n=len(strs)
        for i in range(n):
            for j in range(i+1,n):
                if self.isSafe(strs[i],strs[j]):
                    adj[i].append(j)
                    adj[j].append(i)
        count=0
        vis=[False]*n
        for i in range(n):
            if not vis[i]:
                count+=1
                self.dfs(i,vis,adj)
        return count

    def isSafe(self,s1,s2):
        c=0
        for i in range(len(s1)):
            if s1[i]!=s2[i]:
                c+=1
            if c>2:
                return False
        return True
        
    def dfs(self,node,vis,adj):
        vis[node]=True
        for i in adj[node]:
            if not vis[i]:
                self.dfs(i,vis,adj)
            
            


        