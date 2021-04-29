from numpy import matrix


def sudoku(puzzle):
    """return the solved puzzle as a 2d array of 9 x 9"""
    def is_valid(num, row, col):
        """
        Returns if number is valid assumption for row, col in puzzle
        :param num: int, the number, 1 - 9
        :param row:
        :param col:
        :return: boolean
        """
        nonlocal puzzle
        if num in puzzle[row]:
            return False
        if num in [puzzle[row][c] for c in range(9)]:
            return False
        quad_rows_range = range((row // 3) * 3, (row // 3) * 3 + 3)
        quad_cols_range = range((col // 3) * 3, (col // 3) * 3 + 3)
        if num in [puzzle[r][c] for r in quad_rows_range for c in quad_cols_range]:
            return False

        return True

    def solve():
        nonlocal puzzle
        for i in range(9):
            for j in range(9):
                if puzzle[i][j] == 0:
                    for n in range(1, 10):
                        if is_valid(n, i, j):
                            puzzle[i][j] = n
                            solve()
                            print(matrix(puzzle))
                            puzzle[i][j] = 0
                    return

    solve()
    return puzzle
    # return is_valid(8, 1, 1)


if __name__ == '__main__':
    puzzle = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
              [6, 0, 0, 1, 9, 5, 0, 0, 0],
              [0, 9, 8, 0, 0, 0, 0, 6, 0],
              [8, 0, 0, 0, 6, 0, 0, 0, 3],
              [4, 0, 0, 8, 0, 3, 0, 0, 1],
              [7, 0, 0, 0, 2, 0, 0, 0, 6],
              [0, 6, 0, 0, 0, 0, 2, 8, 0],
              [0, 0, 0, 4, 1, 9, 0, 0, 5],
              [0, 0, 0, 0, 8, 0, 0, 7, 9]]

    puzzle_solved = sudoku(puzzle)
    print(matrix(puzzle_solved))