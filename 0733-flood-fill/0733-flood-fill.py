class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m=len(image)
        n=len(image[0])
        source=image[sr][sc]
        q=deque([(sr,sc)])
        while q:
            i,j=q.popleft()
            if i<0 or j<0 or i>=m or j>=n or image[i][j]==color or image[i][j]!=source:
                continue
            image[i][j]=color
            q.append((i+1,j))
            q.append((i-1,j))
            q.append((i,j+1))
            q.append((i,j-1))
            
        return image
