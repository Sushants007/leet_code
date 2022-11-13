class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        rows, cols = [0] * m, [0] * n
        for i, j in indices:
	        rows[i] = rows[i] ^ 1
	        cols[j] = cols[j] ^ 1
        return sum(ro^col for ro in rows for col in cols)       