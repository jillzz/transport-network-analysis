#!/usr/bin/python
# -*- coding: utf-8 -*-

import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import networkx as nx
from graph_builder import *
from graph_preprocessing import *
from scipy.stats.stats import pearsonr


def main():
    """
    G, nodes_dict = build_graph_networkx('../data/nodes.csv', \
                                         '../data/edges.csv', \
                                         graph_name = 'Multilayer Transport Network (Great Britain)', \
                                         weighted = True)
    remove_self_loops(G)
    remove_isolated_nodes(G)
    """

    # read in data
    data = []
    #N = 267032
    #freq = np.zeros(N)
    with open('../gen_data/only_jumps_weighted.txt', 'r') as in_file:
        for line in in_file:
            data.append(int(line.strip()))
            #i = int(line.strip())
            #freq[i] += 1

    """
    p = np.zeros(N)
    p_dict = nx.pagerank(G, alpha = 0.85, weight = None)
    for i in p_dict:
        p[i] = p_dict[i]

    for i in xrange(len(p)):
        if (not G.has_node(i)):
            p[i] = -1
            freq[i] = -1

    p = [i for i in p if i != -1]
    freq = [i for i in freq if i != -1]

    p_corr = pearsonr(p, freq)

    plt.plot(p, freq, ' ', marker = '.')
    plt.title("Pagerank Jumps - correlation\nP = %f\np-value = %f" % p_corr)
    plt.ylabel("# Jumps from node")
    plt.xlabel("Pagerank")
    plt.axis('tight')
    plt.savefig('../gen_data/figures/pagerank_jumps_corr.pdf')
    """


    min_v = min(data)
    max_v = max(data)

    print min_v
    print max_v

    data = np.asarray(data)
    bins = 100
    #bins = [i for i in range(min_v, max_v+1)]


    plt.hist(data, bins, facecolor = 'red')
    plt.title("Jumps (weighted)")
    plt.ylabel("Frequency")
    plt.xlabel("Distance")
    plt.axis('tight')
    plt.savefig('../gen_data/figures/fig_only_jumps_weighted.pdf')


    """
    data = np.asarray(data)
    sns.set_palette("deep", desat=.6)
    sns.set_context(rc={"figure.figsize": (8, 4)})


    sns.kdeplot(data, bw = 0.1, shade = True)
    plt.savefig("../gen_data/figures/fig2J.pdf", dpi=300)
    print 'Figure 1 plotted'


    sns.distplot(data);
    plt.savefig("../gen_data/figures/fig3J.pdf", dpi=300)
    print 'Figure 2 plotted'

    plt.hist(data, 100)
    plt.savefig("../gen_data/figures/fig1JF.pdf", dpi=300)
    print 'Figure 3 plotted'


    sns.boxplot(data);
    plt.savefig("../gen_data/figures/fig4J.pdf", dpi=300)
    print 'Figure 4 plotted'
    """


#-------------------------------------------------------------------------------

if __name__ == '__main__':
    main()
