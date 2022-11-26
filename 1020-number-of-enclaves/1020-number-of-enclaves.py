class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        d=[[-1,0],[0,1],[1,0],[0,-1]]
        q=[]
        count=0
        r=len(grid)
        c=len(grid[0])
        for i in range(0,r):
            for j in range(0,c):
                if i==0 or j==0 or i==r-1 or j==c-1:
                    if grid[i][j]==1:
                        grid[i][j]=-1
                        q.append((i,j))
                # if board[i][0]==1:
                #     board[i][0]=-1
                #     q.append((i,0))
                # if board[i][c-1]==1:
                #     board[i][c-1]=-1
                #     q.append((i,c-1))
                # if board[0][j]==1:
                #     board[0][j]=-1
                #     q.append((0,j))
                # if board[r-1][j]==1:
                #     board[r-1][j]=-1
                #     q.append((r-1,j))

        while q:
            curr=q[0]
            q.remove(q[0])
            row=curr[0]
            col=curr[1]
            for di,dj in d:
                curRow=row+di
                curCol=col+dj
                if curRow>=1 and curCol>=1 and curRow<r-1 and curCol<c-1 and grid[curRow][curCol]==1:
                    grid[curRow][curCol]=-1
                    q.append((curRow,curCol))
        for i in range(r):
            for j in range(c):  
                    if(grid[i][j]==1):
                        count+=1
        return count                