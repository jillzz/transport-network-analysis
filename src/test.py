from graph_builder import *
from graph_preprocessing import *
from graph_visualization import *
from graph_info import *


def main ():
    G, nodes_dict = build_graph_networkx('../data/nodes.csv', \
                                         '../data/edges.csv', \
                                         graph_name = 'Multilayer Transport Network', \
                                         weighted = False)
    remove_self_loops(G)
    #draw_graph(G)

    #print nx.info(G)
    #output_conectivity_info(G, '../gen_data/conectivity.txt')
    output_indegree_centrality_info (G, '../gen_data/indegree_centrality1.txt', nodes_dict)
    output_outdegree_centrality_info (G, '../gen_data/outdegree_centrality1.txt', nodes_dict)


if __name__ == '__main__':
    main()
