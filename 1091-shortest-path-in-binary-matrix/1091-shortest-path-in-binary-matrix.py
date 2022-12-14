class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0]!=0 or grid[len(grid)-1][len(grid)-1]!=0:
            return -1
        n=len(grid)
        dire=[(1,0),(0,1),(1,1),(-1,0),(0,-1),(-1,-1),(1,-1),(-1,1)]
        q=deque()
        q.append((0,0,1))
        
        while q:
            x,y,dist=q.popleft()
            if x==n-1 and y==n-1:
                return dist
            for d1,d2 in dire:
                a= x+ d1
                b= y+ d2
                if 0<=a<n and 0<=b<n:
                    if grid[a][b]!=1:
                        grid[a][b]=1
                        q.append((a,b,dist+1))
        return -1