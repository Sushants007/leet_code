from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0   
        count = 0
        check = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] =='1' and check[i][j]== False:
                    count += 1
                    self.bfs(grid,check,i,j)
        return count       
    def bfs(self,grid,check,i,j):
        qu = deque([(i,j)])
        while qu:
            i, j = qu.popleft()
            if 0<=i<len(grid) and 0<=j<len(grid[0]) and grid[i][j]=='1' and check[i][j]==False:
                check[i][j] = True
                qu.extend([(i-1,j),(i+1,j),(i,j-1),(i,j+1)])
                
    # def bfs(self,grid,check,i,j):
    #     q=deque((i,j))
    #     n=len(grid)
    #     m=len(grid[0])
    #     while q:
    #         row,col=q.popleft()
    #         for a in range(-1,1,1):
    #             for b in range(-1,1,1):
    #                 nrow=row+a
    #                 ncol=col+b
    #                 if nrow>=0 and nrow<n and ncol>=0 and ncol<m and grid[nrow][ncol] =='1'and check[nrow][ncol]!=1:
    #                     q.extend((nrow,ncol))
