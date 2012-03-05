#!/usr/bin/env python
# encoding: utf-8

import csv
import networkx as nx
import os
import sys

def add_edge_or_weight(G, f, t):
    """
    This function adds a new edge value to the list or increases the weight
    of an existing value.
    """
    if G.has_edge(f,t):
        G[f][t]['weight']+=1
    else:
        G.add_edge(f,t,weight=1)
    return G

def create_edgelist(csv_file, node, edge, edge_file=None):

    '''
    This function takes a csv and turns it the file into an edge list for a
    two mode network.

    Output is either a edgelist file or a graph.

    There are three required values, one optional.
    csv=sys.argv[1]  - The first sys arg is the location of the raw data.
    node=sys.argv[2] - The second is the header row that you want to be nodes.
    edge=sys.argv[3] - The third is the header row that you want to be the edges
                        connecting the nodes.
    edge_file=None  - The forth and option one is the output file.
                            Requires .csv.

    Header in sample data file:
    ['SUPPLIER_FULL_ADDRESS', 'SUPPLIER_CITY', 'PO_NUMBER', 'PO_TOTAL_AMOUNT',
    'NIGP_DESCRIPTION', 'AGENCY_NAME', 'SUPPLIER_STATE', 'SUPPLIER',
    'ORDER_DATE']

    Example:
    sys.argv[2] = 'AGENCY_NAME'
    sys.argv[3] = 'SUPPLIER'

    '''

    # Open and load csv file
    csv_file = csv.DictReader(open(csv_file, "rb"))

    # Let's look for our edges
    # If the value we are using for edges is the same between two nodes,
    # we create an edge

    node_edge_list = []
    for row in csv_file:
        node_edge_list.append((row[node],row[edge]))

    # f & t below stand for 'from' & 'to'
    # In this example, it is not that important, because the graph is undirected,
    # as opposed to directed.
    G = nx.Graph()
    for f in node_edge_list:
        for t in node_edge_list:
            if t != f:
                if f[1] == t[1]:
                    add_edge_or_weight(G, f[0], t[0])

    # Write edges out to a file or return as a Graph.
    if edge_file:
        out = csv.writer(open(edge_file,'wb'), delimiter=',',quotechar='"')
        for edge in G.edges(data=True):
            row = (edge[0], edge[1], str(edge[2]['weight']))
            out.writerow(row)
    else:
        return G


if __name__ == "__main__":

    # Establish out file
    try:
        outfile = sys.argv[4]
    except IndexError:
        outfile = 'edgelist.csv'

    create_edgelist(sys.argv[1], sys.argv[2], sys.argv[3], outfile)