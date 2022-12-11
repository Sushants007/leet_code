class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n=len(graph)
        end=(1<<n)-1
        path=0
        que=deque()
        visited=set()
        
        for i in range(n):
            que.append((i,1<<i))
            
        while que:
            for i in range(len(que)):
                node,cur=que.popleft()
                
                if cur==end:
                    return path
                
                if (node,cur) in visited:
                    continue
                
                visited.add((node,cur))
                for nex in graph[node]:
                    que.append((nex,cur| 1<<nex))
            path+=1
        return -1