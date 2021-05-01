from queue import SimpleQueue


def escape_maze():
    maze = []
    maze.append(['#', '#', 'O', '#', '#', '#', '#'])
    maze.append(['#', ' ', ' ', ' ', '#', ' ', '#'])
    maze.append(['#', ' ', '#', ' ', '#', ' ', '#'])
    maze.append(['#', ' ', '#', ' ', ' ', ' ', '#'])
    maze.append(['#', ' ', '#', '#', '#', ' ', '#'])
    maze.append(['#', ' ', ' ', ' ', '#', ' ', '#'])
    maze.append(['#', '#', '#', '#', '#', 'X', '#'])

    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    visited = [row[:] for row in maze]

    p_end = (6, 5)

    p0 = (0, 2)
    q = SimpleQueue()
    q.put(p0)
    time = 0
    while not q.empty():
        for _ in range(q.qsize()):
            x = q.get()
            visited[x[0]][x[1]] = str(time)
            if x[0] == p_end[0] and x[1] == p_end[1]:
                return visited

            for d in directions:
                p1 = (x[0]+d[0], x[1]+d[1])
                if visited[p1[0]][p1[1]] in ' X':
                    q.put(p1)
        time += 1

    return None


if __name__ == '__main__':
    print(escape_maze())





