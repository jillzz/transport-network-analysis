from graph_builder import *
from graph_preprocessing import *
from graph_visualization import *


def main ():
    G, nodes_dict = build_graph_networkx('../data/nodes.csv', '../data/edges.csv')
    remove_self_loops(G)
    print nx.info(G)
    draw_graph(G)


if __name__ == '__main__':
    main()
