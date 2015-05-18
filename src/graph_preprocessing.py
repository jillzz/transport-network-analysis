#!/usr/bin/python
# -*- coding: utf-8 -*-

import networkx as nx

def remove_self_loops (graph):
    for node in graph.nodes_with_selfloops():
        graph.remove_edge(node, node)


def remove_isolated_nodes (graph):
    for node in nx.isolates(graph):
        graph.remove_node(node)


def set_transition_probabilities(graph):
    for node in graph.nodes_iter():
        weights_sum = 0.0
        for neighbor in graph.neighbors_iter(node):
            weights_sum += graph.get_edge_data(node, neighbor)['weight']

        for neighbor in graph.neighbors_iter(node):
            transition = graph.get_edge_data(node, neighbor)['weight'] / weights_sum
            nx.set_edge_attributes(graph, 'transition', {(node, neighbor): transition})


