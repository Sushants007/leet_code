class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        mp={}
        for i in range(len(graph)):
            mp[i]=graph[i]
        
        def bfs(node,color,mp):
            color[node]=1
            que=deque([node])
            while que:
                ele = que.popleft()
                for i in mp[ele]:
                    if color[i]==-1:
                        color[i]=1-color[ele]
                        que.append(i)
                    elif color [i]==color[ele]:
                        return False
            return True
        
        color=[-1]*len(mp)
        for i in range(len(mp)):
            if color[i]==-1:
                if not bfs(i,color,mp):
                    return False
        return True
