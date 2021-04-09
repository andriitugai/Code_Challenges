class Vertex:
    def __init__(self, name):
        self.name = name
        self.neighbors = []

        self.discovery_time = 0
        self.finish_time = 0
        self.color = 'black'

    def add_neighbor(self, neighbor):
        if neighbor not in self.neighbors:
            self.neighbors.append(neighbor)
            self.neighbors.sort()


class Graph:
    def __init__(self):
        self.vertices = {}
        self.time = 0

    def add_vertex(self, vertex):
        if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex
            return True
        else:
            return False

    def add_edge(self, u, v):
        if u in self.vertices and v in self.vertices:
            for key, value in self.vertices.items():
                if key == u:
                    value.add_neighbor(v)
                elif key == v:
                    value.add_neighbor(u)
            return True
        else:
            return False

    def print_graph(self):
        for key in sorted(self.vertices.keys()):
            print(key + str(self.vertices[key].neighbors) + " " +
                          str(self.vertices[key].discovery_time) + "/" +
                          str(self.vertices[key].finish_time)
                  )

    def _dfs(self, vertex):
        vertex.color = 'red'
        vertex.discovery_time = self.time
        self.time += 1
        for v in vertex.neighbors:
            if self.vertices[v].color == 'black':
                self._dfs(self.vertices[v])
        vertex.color = 'blue'
        vertex.finish_time = self.time
        self.time += 1

    def dfs(self, vertex):
        self.time = 1
        self._dfs(vertex)


if __name__ == '__main__':

    g = Graph()
    vertices = {}
    for i in range(ord('A'), ord('K')):
        name = chr(i)
        vertex = Vertex(name=name)
        vertices[name] = vertex
        g.add_vertex(vertex)

    edges = ['AB', 'AE', 'BF', 'CG', 'DE', 'DH', 'EH', 'FG', 'FI', 'FG', 'GJ', 'HI']

    for edge in edges:
        # g.add_edge(edge[0], edge[1])
        g.add_edge(*edge)

    g.dfs(vertices['A'])
    g.print_graph()
