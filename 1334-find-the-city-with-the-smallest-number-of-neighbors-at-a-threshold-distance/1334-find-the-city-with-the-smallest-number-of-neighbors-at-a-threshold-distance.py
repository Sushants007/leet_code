class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        dist = [[float('inf')] * n for i in range(n)]
        for i in range(n):
            dist[i][i] = 0
        for i, j, w in edges:
            dist[i][j] = w
            dist[j][i] = w
        min_distance = [0] * n
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    new_dist = dist[i][k] + dist[k][j]
                    if dist[i][j] > new_dist:
                        dist[i][j] = new_dist

        res, min_count, min_distance = 0, float('inf'), [0] * n
        for i in range(n):
            min_distance[i] = sum([dist[i][j] <= distanceThreshold for j in range(n)])
            if min_count >= min_distance[i]:
                res = i
                min_count = min_distance[i]
        return res