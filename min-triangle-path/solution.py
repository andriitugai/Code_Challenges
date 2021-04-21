def minimumTotal(triangle):
    size = len(triangle)
    if size == 1:
        return triangle[0][0]

    row = size - 2
    lower_row = triangle[-1][:]
    while row >= 0:
        upper_row = triangle[row][:]
        for i in range(len(upper_row)):
            upper_row[i] += min(lower_row[i], lower_row[i+1])
        lower_row = upper_row
        row -= 1

    return lower_row[0]


if __name__ == '__main__':
    triangle = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
    print(minimumTotal(triangle))
