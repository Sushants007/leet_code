class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n=len(isConnected)
        graph=defaultdict(set)
        visited=set()
        
        for i in range(n):
            for j in range(n):
                if isConnected[i][j]:
                    if i!=j:
                        graph[i].add(j)
                        graph[j].add(i)
                        
        def bfs(node):
            q=deque([node])
            while q:
                node=q.popleft()
                for neighbour in graph[node]:
                    if neighbour not in visited:
                        visited.add(neighbour)
                        q.append(neighbour)
        
        count=0
        for node in range(n):
            if node not in visited:
                visited.add(node)
                bfs(node)
                count+=1
        return count