class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj=collections.defaultdict(list)
        for at,bt,t in flights:
            adj[at].append((bt,t))
        q=deque()
        q.append((0,src,0))
        dist=[math.inf]*n
        dist[src]=0
        
        while q:
            stops,node,cost=q.popleft()
            if stops>k:
                continue
            for nei in adj[node]:
                adjn=nei[0]
                edq=nei[1]
                if cost+edq<dist[adjn] and stops<=k:
                    dist[adjn]=cost+edq
                    q.append((stops+1,adjn,cost+edq))
        if dist[dst]==math.inf:
            return -1
        return dist[dst]
        