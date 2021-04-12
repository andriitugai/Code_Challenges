import itertools

class Solution:
    def largestTriangleArea(self, points) -> float:
        def area(triangle):
            a, b, c = triangle
            return abs(
                a[0] * (b[1] - c[1]) +
                b[0] * (c[1] - a[1]) +
                c[0] * (a[1] - b[1])
            ) / 2

        return max(list(map(area, list(itertools.combinations(points, 3)))))