class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:

        def dfs(row, col, prev_height, ocean):
            """Marks reachable cells with -1
            """
            if row < 0 or col < 0 or row >= num_row or col >= num_col:
                return
            if ocean[row][col] == -1:
                return
            if matrix[row][col] < prev_height:
                return
            ocean[row][col] = -1
            dfs(row + 1, col, matrix[row][col], ocean)
            dfs(row - 1, col, matrix[row][col], ocean)
            dfs(row, col + 1, matrix[row][col], ocean)
            dfs(row, col - 1, matrix[row][col], ocean)

        ans = []
        if not matrix or len(matrix) == 0:
            return ans

        num_row = len(matrix)
        num_col = len(matrix[0])

        ocean_p = [[0] * num_col for _ in range(num_row)]
        ocean_a = [[0] * num_col for _ in range(num_row)]

        for col in range(num_col):
            dfs(0, col, -100, ocean_p)
            dfs(num_row - 1, col, -100, ocean_a)

        for row in range(num_row):
            dfs(row, 0, -100, ocean_p)
            dfs(row, num_col - 1, -100, ocean_a)

        for row in range(num_row):
            for col in range(num_col):
                if ocean_p[row][col] == -1 and ocean_a[row][col] == -1:
                    ans.append([row, col])

        return ans
