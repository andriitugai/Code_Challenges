class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        # from collections import deque
        from queue import LifoQueue

        visited = set([0])
        stack = LifoQueue()

        stack.put(0)
        while not stack.empty():
            keys = rooms[stack.get()]
            for key in keys:
                if key not in visited:
                    visited.add(key)
                    stack.put(key)

        return len(visited) == len(rooms)
