class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        edges = {}
        for row in range(len(wall)):
            edge = 0
            for brick in wall[row]:
                edge += brick
                edges[edge] = edges.get(edge, 0) + 1

        right_edge = max(edges.keys())

        e = [v for k, v in edges.items() if k != right_edge]
        if not e:
            return len(wall)

        return len(wall) - max(e)
