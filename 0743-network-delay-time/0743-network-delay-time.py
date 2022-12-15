class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        poora_time=[0] +[float('inf')]*n
        heap=deque()
        heap.append((0,k))
        graph=defaultdict(list)
        for start,end,time in times:
            graph[start].append((end,time))
        while heap:
            time, node=heap.popleft()
            if time<poora_time[node]:
                poora_time[node]=time
                for i,t in graph[node]:
                    heap.append((time+t,i))
                    
        mx=max(poora_time)
        return mx if mx < float("inf") else -1        