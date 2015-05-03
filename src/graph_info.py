#!/usr/bin/python
# -*- coding: utf-8 -*-

import networkx as nx


def dict_to_sorted_list (dictionary):
    """Utilitiy - builds sorted (by value) list of tuples out of dictionary"""
    dict_list = [item for item in dictionary.items()]
    dict_list.sort(key = lambda tup: tup[1], reverse = True)
    return dict_list


def output_conectivity_info (graph, path):
    """Output strong connectivity information about the graph.
       graph : (networkx.Graph)
       path: (String) contains the path to the output file
    """
    with open(path, 'w') as out:
        out.write('***Conectivity***\n')
        out.write('Is strongly connected: %s\n' % nx.is_strongly_connected(graph))
        out.write('Number of strongly connected components: %d' % nx.number_strongly_connected_components(graph))


def output_indegree_centrality_info (graph, path, nodes_dict):
    """Output In-degree centrality information about the graph.
       graph : (networkx.Graph)
       path: (String) contains the path to the output file
       nodes_dict: (dictionary) maps node id to node name
    """
    indeg_dict = nx.in_degree_centrality(graph)
    indeg_dict = dict((nodes_dict[key], indeg_dict[key]) for key in nodes_dict)
    indeg_list = dict_to_sorted_list(indeg_dict)

    with open(path, 'w') as out:
        out.write('***In-Degree Centrality***\n')
        out.write('Node\tLayer\tIn-degree centrality\n')
        for element in indeg_list:
            out.write('%d\t%d\t%f\n' % (element[0][0], element[0][1], element[1]))


def output_outdegree_centrality_info (graph, path, nodes_dict):
    """Output Out-degree centrality information about the graph.
       graph : (networkx.Graph)
       path: (String) contains the path to the output file
       nodes_dict: (dictionary) maps node id to node name
    """
    outdeg_dict = nx.out_degree_centrality(graph)
    outdeg_dict = dict((nodes_dict[key], outdeg_dict[key]) for key in nodes_dict)
    outdeg_list = dict_to_sorted_list(outdeg_dict)

    with open(path, 'w') as out:
        out.write('***Out-Degree Centrality***\n')
        out.write('Node\tLayer\tOut-degree centrality\n')
        for element in outdeg_list:
            out.write('%d\t%d\t%f\n' % (element[0][0], element[0][1], element[1]))

