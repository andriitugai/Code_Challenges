class Solution:
    def minimumPathCost(self, triangle):
        '''
        :type triangle: list of list of int
        :rtype: int
        '''
        height = len(triangle)

        row = height - 2
        while row >= 0:
            for i in range(row + 1):  # the number elements in equal the # of the row
                triangle[row][i] += min(triangle[row + 1][i], triangle[row + 1][i + 1])

            row -= 1

        print(triangle)

        return triangle[0][0]
