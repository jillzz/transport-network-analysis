from graph_builder import *
from graph_preprocessing import *
from graph_visualization import *
from graph_info import *


def main ():
    G, nodes_dict = build_graph_networkx('../data/nodes.csv', \
                                         '../data/edges.csv', \
                                         graph_name = 'Multilayer Transport Network (Great Britain)', \
                                         weighted = True)
    remove_self_loops(G)
    #draw_graph(G)

    #output_basic_info (G, '../gen_data/basic_graph_info.txt')
    #output_conectivity_info(G, '../gen_data/conectivity.txt')
    output_aperiodicity_info(G, '../gen_data/aperiodicity.txt')
    #output_indegree_centrality_info (G, '../gen_data/indegree_centrality.txt', nodes_dict)
    #output_outdegree_centrality_info (G, '../gen_data/outdegree_centrality.txt', nodes_dict)
    #output_closeness_centrality_info (G, '../gen_data/closeness_centrality.txt', nodes_dict)
    #output_betweeness_centrality_info (G, '../gen_data/betweeness_centrality.txt', nodes_dict)


if __name__ == '__main__':
    main()
