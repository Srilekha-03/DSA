class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        rank=[0]*26
        parent=[0]*26
        for i in range(26):
            parent[i]=i
        def find(x):
            if x==parent[x]:
                return x
            parent[x]=find(parent[x])
            return parent[x]
        def union(x,y):
            parent_x=find(x)
            parent_y=find(y)
            if parent_x==parent_y:
                return
            if rank[parent_x]>rank[parent_y]:
                parent[parent_y]=parent_x
            elif rank[parent_x]<rank[parent_y]:
                parent[parent_x]=parent_y
            else:
                parent[parent_x]=parent_y
                rank[parent_y]+=1
        for s in equations:
            if s[1]=="=":
                union(ord(s[0])-ord('a'),ord(s[3])-ord('a'))
        for s in equations:
            if s[1]=="!":
                parent_x=find(ord(s[0])-ord('a'))
                parent_y=find(ord(s[3])-ord('a'))
                if parent_x==parent_y:
                    return False
        return True