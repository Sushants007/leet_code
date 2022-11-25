class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m=len(image)
        n=len(image[0])
        colortochange=image[sr][sc]
        def dfs(i,j):
            if i<0 or j<0 or i>=m or j>=n or image[i][j]==color or image[i][j]!=colortochange:
                return 0
            image[i][j]=color
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j-1)
            dfs(i,j+1)
        dfs(sr,sc)
        return image
