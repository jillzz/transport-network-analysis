#!/usr/bin/python
# -*- coding: utf-8 -*-

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
    remove_isolated_nodes(G)


    """
    draw_graph(G)

    output_basic_info (G, '../gen_data/basic_graph_info.txt')
    output_conectivity_info(G, '../gen_data/conectivity.txt')
    output_aperiodicity_info(G, '../gen_data/aperiodicity.txt')
    output_indegree_centrality_info (G, '../gen_data/indegree_centrality.txt', nodes_dict)
    output_outdegree_centrality_info (G, '../gen_data/outdegree_centrality.txt', nodes_dict)
    output_closeness_centrality_info (G, '../gen_data/closeness_centrality.txt', nodes_dict)
    output_eigenvector_centrality_info (G, '../gen_data/eigenvector_centrality.txt', nodes_dict)
    output_clustering_info (G.to_undirected(), '../gen_data/clustering.txt', nodes_dict)
    output_pagerank_info (G, '../gen_data/pagerank.txt', nodes_dict, damping = 1)
    output_edge_betweeness_centrality_info (G, '../gen_data/edge_betweeness_centrality.txt', nodes_dict)
    output_betweeness_centrality_info (G, '../gen_data/betweeness_centrality.txt', nodes_dict, 1000)
    output_shortest_path_info (G, '../gen_data/shortest_paths.txt', nodes_dict, weighted = True)
    output_pagerank_info (G, '../gen_data/pagerank7000.txt', nodes_dict, damping = 0.85)
    """


    with open('../gen_data/pagerank1000.txt', 'r') as in_file:
        k = 1
        with open('../gen_data/shortest_paths50.txt', 'w') as out_file:
            for line in in_file:
                k += 1
                source = int(line.split('\t')[0])
                d = nx.single_source_dijkstra_path_length(G, source, weight='weight')
                for key in d:
                    out_file.write('%d\t%d\t%d\n' % (source, key, d[key]))
                if k >= 50:
                    break



if __name__ == '__main__':
    main()
