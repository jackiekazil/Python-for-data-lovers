#!/usr/bin/env python

'''
Please come back later
'''

import csv
import sys
import networkx as nx

CENTRALITY_MAP = (
    ('degree', nx.degree(G)),
    ('closeness', nx.closeness_centrality(G)),
    ('betweeness', nx.betweenness_centrality(G)),
    ('pagerank', nx.pagerank(G)),
)

def sorted_centrality(G,centrality):
    if CENTRALITY_MAP[0] == centrality:
        map = CENTRALITY_MAP[1]
    ms = sorted(map.iteritems(), key=lambda (k,v): (-v,k))
    return ms

def create_graph(edgelist_source):

    G = nx.Graph()
    edge_list = csv.reader(open(edgelist_source))

    for edge in edge_list:
        G.add_edge(edge[0], edge[1], weight=int(edge[2]))
    return G

def generate_centralities(G, results=100, **args):
    '''
    Becareful when running this funciton. Some of the centrality calculations can
    take a very long time. On larger datasets this should probably not be
    preformed on a your personal laptop.

    So, we have specified false for each centrality being run. You have to
    explicity call the centrality.

    Results returned is equal to 100. If you want all the results, set
    results_limit = None.
    '''
    centralities = {}

    # Add one to the results to include the last result
    results = results + 1

    for arg in args:
        centralities[arg] = sorted_centrality(G, arg)[:results]

    return centralities


def main(cents_to_measure, edgelist, centrality_outfile):
    G = create_graph(edgelist)

    # TODO: call generate centralities for cents
    # TODO: Create a function to write out the centralities generated to a file




if __name__ == "__main__":

    edgelist = sys.argv[1]
    centrality_outfile = sys.argv[2]
    cents_to_measure = sys.argv[3]

    main(cents_to_measure, edgelist, centrality_outfile)