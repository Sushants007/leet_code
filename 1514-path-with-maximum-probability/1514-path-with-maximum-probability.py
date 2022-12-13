class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        adj_list = {i: [] for i in range(0, n)}
        
        for e, w in zip(edges, succProb):
            v1, v2 = e
            adj_list[v1].append((w, v2))
            adj_list[v2].append((w, v1))
        
        max_heap = [(-1, start)]
        seen = set()

        
        while max_heap:
            weight, v =heappop(max_heap)            
            
            if v in seen: continue
            if v == end: return -weight
            
            seen.add(v)
            
            for neighbor_weight, neighbor in adj_list[v]:
                if neighbor not in seen:
                    heappush(max_heap, (weight * neighbor_weight, neighbor))
        
        return 0.0
