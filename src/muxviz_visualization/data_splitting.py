#!/usr/bin/python
# -*- coding: utf-8 -*-

import csv


def main ():
    layers = [open('splitted/air.txt', 'w'), \
              open('splitted/ferry.txt', 'w'), \
              open('splitted/rail.txt', 'w'), \
              open('splitted/metro.txt', 'w'), \
              open('splitted/coach.txt', 'w'), \
              open('splitted/bus.txt', 'w')]

    with open('../../data/edges.csv', 'r') as edges_data:
        csv_reader = csv.reader(edges_data)
        csv_reader.next()
        for row in csv_reader:
            if row[2] == row[3] and row[0] != row[1]:
                i = int(row[2])
                layers[i].write('%s %s %s\n' % (row[0].strip(), row[1].strip(), row[4].strip()))

    for l in layers:
        l.close()

    with open('../../data/nodes.txt', 'w') as nodes_data:
        for i in xrange(267031):
            nodes_data.write('%d %d\n' % (i, i))




if __name__ == '__main__':
    main()
