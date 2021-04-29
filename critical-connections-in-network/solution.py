from collections import defaultdict


class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(set)
        for src, dst in connections:
            graph[src].add(dst)
            graph[dst].add(src)

        visited = set()
        lowest = [0] * n

        result = []

        def dfs(rank, prev_vertex, curr_vertex):
            visited.add(curr_vertex)
            lowest[curr_vertex] = rank

            for child in graph[curr_vertex]:
                if child == prev_vertex:
                    continue
                if child not in visited:
                    dfs(rank + 1, curr_vertex, child)
                if lowest[child] == rank + 1:
                    result.append([curr_vertex, child])
                lowest[curr_vertex] = min(lowest[curr_vertex], lowest[child])

            return lowest

        dfs(0, -1, 0)

        return result

