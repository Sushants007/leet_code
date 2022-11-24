class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        if not isConnected:
            return 0
        n=len(isConnected)
        visit=[0]*n
        def dfs(u):
            for v in range(n):
                if isConnected[u][v]==1 and visit[v]==0:
                    visit[v]=1
                    dfs(v)
        count=0
        for i in range(n):
            if visit[i]==0:
                count+=1
                visit[i]=1
                dfs(i)
        return count