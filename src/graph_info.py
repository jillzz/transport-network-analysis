#!/usr/bin/python
# -*- coding: utf-8 -*-

import networkx as nx


def output_conectivity_info (graph, path):
    with open(path, 'w') as out:
        out.write('***Conectivity***\n')
        out.write('Is strongly connected: %s\n' % nx.is_strongly_connected(graph))
        out.write('Number of strongly connected components: %d' % nx.number_strongly_connected_components(graph))

