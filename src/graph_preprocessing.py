#!/usr/bin/python
# -*- coding: utf-8 -*-

import networkx as nx

def remove_self_loops(graph):
    for node in graph.nodes_with_selfloops():
        graph.remove_edge(node, node)
    #for node in nx.nodes(graph):
    #    if graph.has_edge(node, node):
    #        graph.remove_edge(node, node)
