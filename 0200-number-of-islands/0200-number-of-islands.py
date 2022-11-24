class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    print(i,j)
                    self.dfs(grid,i,j)
                    count  += 1
        #print(grid)
        return count
    # use a helper function to flip connected '1's to 0
    def dfs(self,grid,i,j):
        grid[i][j] = 0
        for dr,dc in (1,0), (-1,0), (0,-1), (0,1):
            r = i + dr
            c = j + dc
            if 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c]=='1':
                self.dfs(grid,r,c)

                
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
