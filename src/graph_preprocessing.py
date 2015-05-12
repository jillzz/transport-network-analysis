#!/usr/bin/python
# -*- coding: utf-8 -*-

import networkx as nx

def remove_self_loops (graph):
    for node in graph.nodes_with_selfloops():
        graph.remove_edge(node, node)


def remove_isolated_nodes (graph):
    for node in nx.isolates(graph):
        graph.remove_node(node)