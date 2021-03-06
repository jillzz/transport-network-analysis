#!/usr/bin/python
# -*- coding: utf-8 -*-

import csv
import snap
import networkx as nx


def read_csv (path):
    """ Read in the data from the csv file and return it as
        matrix of strings:
        path: the path to the file
    """
    with open(path, 'r') as csvfile:
        csv_reader = csv.reader(csvfile)
        csv_reader.next()
        data = [row for row in csv_reader]

    return data


def read_nodes (path):
    """ Read in the nodes as dictionary (node, layer) is mapped to node_id
    """
    data = read_csv(path)
    nodes_dict = dict ( ( ( int(data[i][0].strip()), int(data[i][1].strip()) ), i ) \
          for i in xrange(len(data)) )
    return nodes_dict


def read_edges (path):
    """ Read in the edges as list where each element is another list of type
        [(ori_node, ori_layer), (des_node, des_layer), weight]
    """
    data = read_csv(path)
    edges_list = [ [ (int(row[0]), int(row[2])) , (int(row[1]), int(row[3])) , int(row[4]) ] \
                 for row in data ]
    return edges_list


def build_graph_snap (nodes_file, edges_file):
    """ Builds the graph as snap.TNGraph (weighted, directed graph)
    """
    nodes_data = read_nodes (nodes_file)
    edges_data = read_edges (edges_file)
    graph = snap.TNGraph.New()

    for node in nodes_data.keys():
        graph.AddNode (nodes_data[node])

    for edge in edges_data:
        graph.AddEdge (nodes_data[edge[0]], nodes_data[edge[1]])

    inv_nodes = {v: k for k, v in nodes_data.items()}
    return graph, inv_nodes


def build_graph_networkx (nodes_file, edges_file, graph_name = 'Graph', weighted = True):
    """Build NetworkX based directed graph"""
    graph = nx.DiGraph(name = graph_name)
    nodes_data = read_nodes (nodes_file)
    edges_data = read_edges (edges_file)
    graph.add_nodes_from(nodes_data.values())
    for edge in edges_data:
        """
        if edge[0][1] == 3 and edge[1][1] == 3:
            if weighted:
                graph.add_edge(nodes_data[edge[0]], nodes_data[edge[1]], {'weight': edge[2]})
            else:
                graph.add_edge(nodes_data[edge[0]], nodes_data[edge[1]])
        """
        if weighted:
            graph.add_edge(nodes_data[edge[0]], nodes_data[edge[1]], {'weight': edge[2]})
        else:
            graph.add_edge(nodes_data[edge[0]], nodes_data[edge[1]])


    inv_nodes = {v: k for k, v in nodes_data.items()}
    return graph, inv_nodes




