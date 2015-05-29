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

N = 267031            # number of nodes

def read_in_shortest_paths(path):
    with open(path) as in_file:
        for line in in_file:
            tokens = line.split('\t')
            shortest_paths_memo[(int(tokens[0]), int(tokens[1]))] = int(tokens[2])


#------------------------------------------------------------------------------

def simulate_random_walk (G, damping, max_jumps):
    """ Random walk simulation on weighted graph G with damping factor d
        and max_jumps as maximum number of jumps"""

    results = []
    nodes = [] # keep nodes
    current_node = random.randrange(N)
    while not G.has_node(current_node):
        current_node = random.randrange(N)

    j = 0
    while (j < max_jumps):
        previous_node = current_node
        jump_decision = random.uniform(0, 1)

        if jump_decision < damping or G.out_degree(current_node) == 0:
            # make a jump
            current_node = random.randrange(N)
            while not G.has_node(current_node):
                current_node = random.randrange(N)

            j += 1
            try:
                distance = nx.astar_path_length(G, previous_node, \
                               current_node, weight = 'weight')
                # distance intervals 1h traveling
                results.append(distance)
                nodes.append(previous_node)
            except nx.NetworkXNoPath: continue

        else:
            # move to neighbor node
            incident = G.out_edges([current_node], data = False)
            distribution = [ G.get_edge_data(e[0], e[1])['transition'] for e in incident ]
            xk = np.arange(len(incident))
            generator = stats.rv_discrete(values = (xk, distribution))
            current_node = incident[generator.rvs()][1]

    return results, nodes


#-------------------------------------------------------------------------------

def simulate_random_walk_unweighted (G, damping, max_jumps):
    """ Random walk simulation on unweighted graph G with damping factor d
        and max_jumps as maximum number of jumps"""

    results = []
    nodes = [] # keep nodes
    current_node = random.randrange(N)
    while not G.has_node(current_node):
        current_node = random.randrange(N)


    j = 0
    while (j < max_jumps):
        previous_node = current_node
        jump_decision = random.uniform(0, 1)

        if jump_decision < damping or G.out_degree(current_node) == 0:
            # make a jump
            current_node = random.randrange(N)
            while not G.has_node(current_node):
                current_node = random.randrange(N)

            j += 1
            try:
                distance = nx.shortest_path_length(G, previous_node, current_node)
                results.append(distance)
                nodes.append(previous_node) # keep nodes
            except nx.NetworkXNoPath: continue

        else:
            # move to neighbor node
            incident = G.out_edges([current_node], data = False)
            current_node = random.choice(incident)[1]

    return results, nodes #, current_node (keep nodes)


#------------------------------------------------------------------------------

def main():
    G, nodes_dict = build_graph_networkx('../data/nodes.csv', \
                                         '../data/edges.csv', \
                                         graph_name = 'Multilayer Transport Network (Great Britain)', \
                                         weighted = True)
    remove_self_loops(G)
    remove_isolated_nodes(G)
    set_transition_probabilities(G)

    print 'MAIN'

    start = time.time()
    data, nodes = simulate_random_walk(G, 0.15, 24000)
    end = time.time()
    print 'Simulation finished in %d min.' % (float(end-start) / 60.0)

    with open('../gen_data/weighted_jumps.txt', 'w') as out:
        for i in data:
            out.write('%d\n' % i)

    with open('../gen_data/weighted_jumps_from.txt', 'w') as out:
        for i in nodes:
            out.write('%d\n' % i)

    """
    data = np.asarray(data)
    sns.set_palette("deep", desat=.6)
    sns.set_context(rc={"figure.figsize": (8, 4)})

    sns.kdeplot(data, bw = 0.1, shade = True)
    #plt.show()
    plt.savefig("../gen_data/figures/fig2.pdf", dpi=300)

    sns.distplot(data);
    #plt.show()
    plt.savefig("../gen_data/figures/fig3.pdf", dpi=300)

    plt.hist(data, 100)
    #plt.show()
    plt.savefig("../gen_data/figures/fig1.pdf", dpi=300)

    sns.boxplot(data);
    #plt.show()
    plt.savefig("../gen_data/figures/fig4.pdf", dpi=300)
    """

#-------------------------------------------------------------------------------

def test():
    G, nodes_dict = build_graph_networkx('../data/nodes.csv', \
                                         '../data/edges.csv', \
                                         graph_name = 'Multilayer Transport Network (Great Britain)', \
                                         weighted = True)
    remove_self_loops(G)
    remove_isolated_nodes(G)
    #set_transition_probabilities(G)

    jumps = 24000
    results = []
    current_node = random.randrange(N)
    while not G.has_node(current_node):
        current_node = random.randrange(N)

    for i in xrange(jumps):
        previous_node = current_node
        current_node = random.randrange(N)
        while not G.has_node(current_node):
            current_node = random.randrange(N)

        try:
            distance = nx.shortest_path_length(G, previous_node, current_node, weight='weight')
            results.append(distance)
        except nx.NetworkXNoPath: continue


    with open('../gen_data/only_jumps_weighted1.txt', 'w') as out:
        for i in results:
            out.write('%d\n' % i)

    """
    data = np.asarray(results)
    sns.set_palette("deep", desat=.6)
    sns.set_context(rc={"figure.figsize": (8, 4)})

    sns.kdeplot(data, bw = 0.1, shade = True)
    #plt.show()
    plt.savefig("../gen_data/figures/fig2J.pdf", dpi=300)

    sns.distplot(data);
    #plt.show()
    plt.savefig("../gen_data/figures/fig3J.pdf", dpi=300)

    plt.hist(data, 100)
    #plt.show()
    plt.savefig("../gen_data/figures/fig1J.pdf", dpi=300)

    sns.boxplot(data);
    #plt.show()
    plt.savefig("../gen_data/figures/fig4J.pdf", dpi=300)
    """

#-------------------------------------------------------------------------------

if __name__ == '__main__':
    test()


