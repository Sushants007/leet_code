class Solution:
	def containsCycle(self, grid: List[List[str]]) -> bool:
		row, col = len(grid), len(grid[0])
		visited = set()

		for x in range(row):
			for y in range(col):
				if (x,y) not in visited:
					queue = deque([(x, y, set([]), None)])
					if self.bfs(queue, row, col, grid[x][y], grid, visited):
						return True

		return False

	def bfs(self, queue, row, col, curVal, grid, visited):
		while queue:
			x, y, curPath, prev = queue.popleft()

			visited.add((x,y))
			curPath.add((x,y))

			for nx, ny in [[x+1,y],[x-1,y],[x,y-1],[x,y+1]]:
				if 0<=nx<row and 0<=ny<col and grid[nx][ny] == curVal:
					if (nx,ny) in curPath and (nx,ny) != prev:
						return True
					if (nx,ny) not in curPath:
						queue.append((nx,ny, curPath, (x,y)))

		return False