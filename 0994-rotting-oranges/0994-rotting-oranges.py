class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        
        if rows ==0:
            return -1
        
        cols=len(grid[0])
        fresh=0
        rotten=deque()
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==2:
                    rotten.append((i,j))
                elif grid[i][j]==1:
                    fresh+=1
                    
        min=0
        
        while rotten and fresh>0:
            
            
            for _ in range(len(rotten)):
                 
                x,y = rotten.popleft()
                for dx,dy in [(0,1),(1,0),(-1,0),(0,-1)]:
                    xx=x+dx
                    yy=y+dy
                    if xx<0 or yy<0 or xx>=rows or yy>=cols: 
                        continue
                    if grid[xx][yy]==0 or grid[xx][yy]==2: 
                        continue
                       
                    fresh-=1
                    grid[xx][yy]=2
                    rotten.append((xx,yy))
            min+=1                    
        if fresh==0:
            return min        
        else:
            return -1        