from queue import SimpleQueue

class Vertex:
    def __init__(self, name):
        self.name = name
        self.neighbors = []
        self.color = 'black'

        self.predecessor = None
        self.discovery_time = -1

    def add_neighbor(self, neighbor):
        if neighbor not in self.neighbors:
            self.neighbors.append(neighbor)
            self.neighbors.sort()

class Graph:
    def __init__(self):
        self.vertices = {}
        self.time = 0

    def add_vertex(self, vertex):
        if isinstance(vertex, Vertex) and vertex.name not in self.vertices.keys():
            self.vertices[vertex.name] = vertex
            return True
        else:
            return False

    def add_edge(self, u, v):
        if u in self.vertices.keys() and v in self.vertices.keys():
            for key, value in self.vertices.items():
                if key == u:
                    value.add_neighbor(v)
                elif key == v:
                    value.add_neighbor(u)
            return True
        else:
            return False

    def bfs(self, starting_vertex):
        q = SimpleQueue()
        q.put(starting_vertex)
        self.time = 1
        while not q.empty():
            # v = q.get()
            # print(v)
            # vertex = self.vertices[v]
            vertex = self.vertices[q.get()]
            for v in vertex.neighbors:
                if self.vertices[v].color == 'black':
                    self.time += 1
                    self.vertices[v].discovery_time = self.time
                    self.vertices[v].color = 'grey'
                    self.vertices[v].predecessor = vertex.name
                    q.put(v)
            vertex.color = 'blue'

    def print_graph(self):
        for key in sorted(self.vertices.keys()):
            print(key, str(self.vertices[key].neighbors),
                str(self.vertices[key].predecessor) + "/" +
                str(self.vertices[key].discovery_time))


if __name__ == '__main__':
    g = Graph()
    vertices = {}
    for i in range(ord('A'), ord('L')):
        name = chr(i)
        vertex = Vertex(name=name)
        vertices[name] = vertex
        g.add_vertex(vertex)

    edges = ['AB', 'BC', 'AE', 'EI', 'BF', 'IF', 'FG', 'GJ', 'GK', 'KH', 'HD']
    for edge in edges:
        g.add_edge(edge[0], edge[1])

    g.bfs("A")

    g.print_graph()
