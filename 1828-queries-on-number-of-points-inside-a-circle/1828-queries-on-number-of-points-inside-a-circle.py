class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        ans = [0] * len(queries)
        for i, query in enumerate(queries):
            r = query[2]
            for point in points:
                distance = sqrt((point[0]-query[0])**2 + (point[1]-query[1])**2)
                if distance <= r:
                    ans[i] += 1
        return ans