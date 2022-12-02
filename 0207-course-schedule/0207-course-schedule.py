class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        indegree = [0] * numCourses

        for child, parent in prerequisites:
            graph[parent].append(child)
            indegree[child]+=1
        queue = deque()
        for i, value in enumerate(indegree):
            if value == 0:
                queue.append(i)

        seq = []
        while queue:
            course = queue.popleft()
            seq.append(course)
            for neighbour in graph[course]:
                indegree[neighbour] -= 1

                if indegree[neighbour] == 0:
                    queue.append(neighbour)

        return len(seq) == numCourses