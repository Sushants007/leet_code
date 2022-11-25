class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        R, C = len(mat), len(mat[0])
        q = []
        visited = set()
        directions = [(0,1), (0,-1), (1, 0), (-1, 0)]
        for r in range(R):
            for c in range(C):
                if mat[r][c]==0 and (r,c) not in visited:
                    q.append((r,c))
                    visited.add((r,c))
                else:
                    mat[r][c]="#"
        for r, c in q:
            for x,y in directions:
                rx, cy = r+x, c+y
                
                if 0<=rx<R and 0<=cy<C and mat[rx][cy]=="#":
                    mat[rx][cy]=mat[r][c]+1
                    q.append((rx, cy))
        return mat