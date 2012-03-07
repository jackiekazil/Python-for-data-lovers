#!/usr/bin/env python

'''
This file takes a csv and turns it into a network graph using networkx.
'''

import csv
import sys
import networkx as nx

def _sorted_map(map):
    ms = sorted(map.iteritems(), key=lambda (k,v): (-v,k))
    return ms

# TODO: Combo functions find_* into one.

def find_greatest_degree(G, output=False):
    deg=nx.degree(G)
    ds=_sorted_map(deg)

    if output:
        print "### Degree output ###"
        for node,value in ds[0:99]:
            print "%s, %s" % (node,value)
    else:
        return ds

def find_greatest_closeness_centrality(G, output=False):

    c = nx.closeness_centrality(G)
    cs = _sorted_map(c)

    if output:
        print "### Closeness Centrality ###"
        for node,value in cs[0:99]:
            print "%s, %s" % (node,value)
    else:
        return cs

def find_greatest_betweenness_centrality(G, output=False):

    b = nx.betweenness_centrality(G)
    bs = _sorted_map(b)

    if output:
        print "### Betweenness Centrality ###"
        for node,value in bs[0:99]:
            print "%s, %s" % (node,value)
    else:
        return bs

def create_graph(edgelist_source):

    G = nx.Graph()
    edge_list = csv.reader(open(edgelist_source))

    for edge in edge_list:
        G.add_edge(edge[0], edge[1], weight=edge[2])
    return G

if __name__ == "__main__":

    edgelist = sys.argv[1]
    G = create_graph(edgelist)

    find_greatest_degree(G, output=True)
    find_greatest_closeness_centrality(G, output=True)
    find_greatest_betweenness_centrality(G, output=True)