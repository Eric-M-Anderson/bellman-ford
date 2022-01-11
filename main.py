from algorithm import NetworkAlgorithm  # https://www.programiz.com/dsa/bellman-ford-algorithm


def read_file(data):
    edges = []
    for i in range(len(data)):
        if i % 3 == 0:
            edges.append([data[i], data[i + 1], int(data[i + 2])])
    return edges


if __name__ == "__main__":
    # path = [['Oshawa', 'Montreal', 499], ['Ottawa', 'Kingston', 500], ['Oshawa', 'Whitby', 9], ['Oshawa', 'Toronto', 61], ['Oshawa', 'Kingston', 205],
    #         ['Oshawa', 'Ottawa', 100], ['Toronto', 'Vancouver', 10], ['Vancouver', 'Ottawa', 10]]
    file_data = open('network.txt').read().split(', ')
    g = NetworkAlgorithm(read_file(file_data))

    start_node = input('What is your start node: ')
    the_map = g.bellman_ford_map(start_node)  # Makes the map

    while True:
        end_node = input('What is your destination: ')
        while True:
            try:
                route_info = g.plot_path(the_map, end_node)
                cost = route_info[0]
                route = route_info[1]
                print(the_map[0])
                break
            except TypeError as e:
                print(e)
                end_node = input('What is your destination: ')

        path_string = ''
        for n in route:
            if route.index(n) < len(route) - 1:
                path_string += '{} --> '.format(n)
            else:
                path_string += n
        print('The path to the destination is ({}) and the distance to your destination is {}.'.format(path_string, cost))
        g.print_graph(route)
        if end_node == 'exit':
            break
