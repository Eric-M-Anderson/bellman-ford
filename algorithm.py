from graph import NetworkGraph


class NetworkAlgorithm(NetworkGraph):
    def __init__(self, paths):
        super().__init__(paths)

    def initialize_bellman_ford(self, source_node):
        initialize_map = {}
        nodes = self.get_nodes()
        for n in nodes:
            if n == source_node:
                initialize_map[n] = 0
            else:
                initialize_map[n] = float('inf')
        return initialize_map

    def bellman_ford_cost(self, source_node):
        iteration = 0
        cost_to = self.initialize_bellman_ford(source_node)
        possible_connections = []
        while iteration < len(self.get_nodes()):
            for node in cost_to.keys():
                node_neighbors = self.get_neighbors(node)
                for neighboring_node in node_neighbors:
                    if self.get_edge_weight(node, neighboring_node) + cost_to[node] < cost_to[neighboring_node]:
                        cost_to[neighboring_node] = self.get_edge_weight(node, neighboring_node) + cost_to[node]
                        possible_connections.append([node, neighboring_node])
            iteration += 1
        return cost_to, possible_connections

    def bellman_ford_map(self, source_node):
        bf_cost_output = self.bellman_ford_cost(source_node)
        cost_to = bf_cost_output[0]
        possible_connections = bf_cost_output[1]

        fastest_connections = []
        get_fastest_connection = []
        for node in self.get_nodes():
            for pc in possible_connections:
                if pc[1] == node:
                    get_fastest_connection.append(pc)
                    fastest_connections.append(get_fastest_connection[len(get_fastest_connection) - 1])

        the_map = []
        for c in fastest_connections:
            if c[0] == source_node:
                the_map.append(c)
        for num in range(len(self.get_nodes())):
            for r in the_map:
                for c in fastest_connections:
                    if r[len(r) - 1] == c[0] and r[len(r) - 1] != c[1]:
                        temp = r.copy()
                        temp.append(c[1])
                        the_map.append(temp)

        return cost_to, the_map

    @staticmethod
    def plot_path(the_map_list, destination_node):
        for p in the_map_list[1]:
            if p[len(p) - 1] == destination_node:
                return the_map_list[0][destination_node], p

    """def bellman_ford_make_map(self, source_node):
        lowest_cost_to = self.initialize_bellman_ford(source_node)
        possible_path = []
        for n in lowest_cost_to.keys():
            node_neighbors = self.get_neighbors(n)
            for nn in node_neighbors:
                if self.get_edge_weight(n, nn) + lowest_cost_to[n] < lowest_cost_to[nn]:
                    lowest_cost_to[nn] = self.get_edge_weight(n, nn) + lowest_cost_to[n]
                    possible_path.append([n, nn])
        fastest_connections = []
        for n in self.get_nodes():
            temp = []
            for p in possible_path:
                if n in p and p.index(n) == 1:
                    temp.append(p)
            length = len(temp) - 1
            if length >= 0:
                fastest_connections.append(temp[length])
        the_map = []
        for c in fastest_connections:
            if c[0] == source_node:
                the_map.append(c)
        for num in range(len(self.get_nodes())):
            for r in the_map:
                for c in fastest_connections:
                    if r[len(r) - 1] == c[0] and r[len(r) - 1] != c[1]:
                        temp = r.copy()
                        temp.append(c[1])
                        the_map.append(temp)
        return lowest_cost_to, the_map"""
