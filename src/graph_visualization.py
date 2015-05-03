#!/usr/bin/python
# -*- coding: utf-8 -*-

import networkx as nx
import matplotlib.pyplot as pyplot

def draw_graph (graph):
    nx.draw(graph)
    pyplot.savefig("test.png")


