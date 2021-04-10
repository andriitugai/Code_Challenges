class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or len(matrix) == 0:
            return 0

        rows = len(matrix)
        cols = len(matrix[0])
        max_path = 0

        mem = [[0] * cols for _ in range(rows)]

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def longest(i, j):
            nonlocal mem, matrix
            if mem[i][j] > 0:
                return mem[i][j]
            max_p = 0
            for d in directions:
                x, y = i + d[0], j + d[1]
                if x > -1 and y > -1 and x < rows and y < cols and matrix[x][y] > matrix[i][j]:
                    max_p = max(max_p, longest(x, y))

            mem[i][j] = max_p + 1
            return mem[i][j]

        for ix in range(rows):
            for jx in range(cols):
                path = longest(ix, jx)
                max_path = max(max_path, path)

        return max_path
