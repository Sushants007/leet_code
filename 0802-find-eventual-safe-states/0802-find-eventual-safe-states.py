class Solution:
    def cycle(self,graph,node,vis):
        if vis[node]==2:
            return True
        vis[node]=2
        for neighbour in graph[node]:
            if vis[neighbour]!=1:
                if self.cycle(graph,neighbour,vis):
                    return True
        vis[node]=1
        return False
    
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n=len(graph)
        vis=[0]*n
        for i in range(n):
            if vis[i]==0:
                if self.cycle(graph,i,vis):
                    continue
        ans=[]
        for i in range(n):
            if vis[i]==1:
                ans.append(i)
        return ans