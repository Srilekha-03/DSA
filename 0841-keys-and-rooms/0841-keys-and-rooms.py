class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n=len(rooms)
        vis=[-1]*n
        self.dfs(rooms,0,vis,n)
        for i in vis:
            if i==-1:
                return False
        return True
    def dfs(self,rooms,start,vis,n):
        vis[start]=0
        for key in rooms[start]:
            if vis[key]==-1:
                self.dfs(rooms,key,vis,n)



        