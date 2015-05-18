#!/usr/bin/python
# -*- coding: utf-8 -*-

import random
import networkx as nx
import numpy as np
import time
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats
from graph_builder import *
from graph_preprocessing import *


shortest_paths_memo = {}

def read_in_shortest_paths(path):
    with open(path) as in_file:
        for line in in_file:
            tokens = line.split('\t')
            shortest_paths_memo[(int(tokens[0]), int(tokens[1]))] = int(tokens[2])


def simulate_random_walk (G, damping, max_jumps):
    """ Random walk simulation on graph G with damping factor d
        and max_jumps as maximum number of jumps"""

    #transition_dict = nx.get_edge_attributes(G, 'transition')
    results = []
    current_node = 24689 #random.randrange(G.order())
    while not G.has_node(current_node):
        current_node = random.randrange(G.order())

    j = 0
    while (j < max_jumps):
        previous_node = current_node
        jump_decision = random.uniform(0, 1)

        if jump_decision < damping or G.out_degree(current_node) == 0:
            # make a jump
            current_node = random.randrange(G.order())
            while not G.has_node(current_node):
                current_node = random.randrange(G.order())

            j += 1
            try:
                distance = nx.astar_path_length(G, previous_node, \
                               current_node, weight = 'weight')
                # distance intervals 1h traveling
                results.append(distance)
            except nx.NetworkXNoPath: continue

        else:
            # move to neighbor node
            incident = G.out_edges([current_node], data = False)
            distribution = [ G.get_edge_data(e[0], e[1])['transition'] for e in incident ]
            xk = np.arange(len(incident))
            generator = stats.rv_discrete(values = (xk, distribution))
            current_node = incident[generator.rvs()][1]

    return results, current_node


def main():
    G, nodes_dict = build_graph_networkx('../data/nodes.csv', \
                                         '../data/edges.csv', \
                                         graph_name = 'Multilayer Transport Network (Great Britain)', \
                                         weighted = True)
    remove_self_loops(G)
    remove_isolated_nodes(G)
    set_transition_probabilities(G)

    start = time.time()
    data, current_node = simulate_random_walk(G, 0.15, 24000)
    end = time.time()
    print 'Simulation finished in %d min.' % (float(end-start) / 60.0)

    with open('../gen_data/results.txt', 'a') as out:
        for i in data:
            out.write('%d,' % i)
        out.write('\n')
        out.write('%d' % current_node)

    data = np.asarray(data)
    sns.set_palette("deep", desat=.6)
    sns.set_context(rc={"figure.figsize": (8, 4)})
    plt.hist(data, 50)
    plt.show()
    sns.kdeplot(data, bw = 0.2, shade = True)
    plt.show()
    sns.distplot(data);
    plt.show()




if __name__ == '__main__':
    main()


