class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        
        def bfs(row,col,visited):
            visited[row][col] = 1
            queue = [[[row,col],[-1,-1]]]
            while queue:
                popped = queue.pop(0)
                row, col = popped[0][0], popped[0][1]
                pr, pc = popped[1][0], popped[1][1]
                
                val = grid[row][col]
                for i in range(4):
                    nrow = row + delrow[i]
                    ncol = col + delcol[i]
                    
                    if nrow >= 0 and nrow < n and ncol >= 0 and ncol < m and grid[nrow][ncol] == val:
                        if not visited[nrow][ncol]:
                            visited[nrow][ncol] = 1
                            queue.append([[nrow,ncol],[row,col]])
                        elif pr != nrow and pc != ncol:
                            return True
            return False
                
        
        
        n = len(grid)
        m = len(grid[0])
        
        delrow = [-1,0,1,0]
        delcol = [0,1,0,-1]

        
        visited = [[0 for _ in range(m)] for _ in range(n)]
        
        for i in range(n):
            for j in range(m):
                if not visited[i][j]:
                    if bfs(i,j,visited):
                        return True
        return False