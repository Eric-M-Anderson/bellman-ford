import networkx as nx
import matplotlib.pyplot as mpl


class NetworkGraph:
    def __init__(self, paths):
        self.paths = paths
        # [['Oshawa', 'Montreal', 499], ['Ottawa', 'Kingston', 500], ['Oshawa', 'Whitby', 9], ['Oshawa', 'Toronto', 61], ['Oshawa', 'Kingston', 205], ['Oshawa', 'Ottawa', 100],
        # ['Toronto', 'Vancouver', 100], ['Vancouver', 'Ottawa', 100]]
        self.the_graph = self.initialize()

    def initialize(self):
        g = nx.DiGraph()  # Declares the directed graph
        added_node = []
        for p in self.paths:
            start_node = p[0]
            end_node = p[1]
            if start_node not in added_node:
                g.add_node(start_node)
                added_node.append(start_node)
            if end_node not in added_node:
                g.add_node(end_node)
                added_node.append(end_node)
            g.add_edges_from([(start_node, end_node)], weight=p[2])
        return g

    def change_weight(self, start_node, end_node, weight):
        self.the_graph.remove_edge(start_node, end_node)
        self.the_graph.add_edges_from([(start_node, end_node)], weight=weight)  # Makes the edge between two nodes

    def add_edge(self, start_node, end_node, weight):
        self.the_graph.add_edges_from([(start_node, end_node)], weight=weight)

    def add_node(self, node):
        self.the_graph.add_node(node)

    def remove_edge(self, start_node, end_node):
        self.the_graph.remove_edge(start_node, end_node)  # removes the edge from node start to node end

    def remove_node(self, node):
        self.the_graph.remove_node(node)  # removes the node

    def get_neighbors(self, node):
        neighbours = list(self.the_graph.neighbors(node))
        return neighbours

    def get_nodes(self):
        return self.the_graph.nodes

    def get_edge_weight(self, start_node, end_node):
        return self.the_graph.get_edge_data(start_node, end_node)['weight']

    def print_graph(self, route=''):
        pos = nx.planar_layout(self.the_graph)

        # pos = nx.spring_layout(self.the_graph)
        weights = nx.get_edge_attributes(self.the_graph, "weight")
        if route == '':
            nx.draw_networkx(self.the_graph, pos, with_labels=True)  # draws the graph
        else:
            not_route = list(self.get_nodes())
            for n in not_route:
                if n in route:
                    not_route.remove(n)
            nx.draw_networkx(self.the_graph, pos, nodelist=not_route, node_color='b', with_labels=True)  # draws the graph
            nx.draw_networkx(self.the_graph, pos, nodelist=route, node_color='r', with_labels=True)  # draws the graph
        nx.draw_networkx_edge_labels(self.the_graph, pos, edge_labels=weights)  # adds the labels
        mpl.show()  # prints the drawn graph
