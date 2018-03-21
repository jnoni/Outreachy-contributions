import networkx as nx
import matplotlib.pyplot as plt
import numpy as np


def watts_strogatz_model(nodes, k, p):
    """
    :param nodes: the number of nodes
    :param k: the number of nearest neighbours, to which each node is connected
    :param p: probability of rewiring each edge
    :return: 2 vectors: normalized clustering coefficient values and average shortest path values
    """
    avg_shortest_path = []
    cluster_coefficient = []
    probability = []
    edges = []
    while p <= 1:
        my_graph = nx.connected_watts_strogatz_graph(nodes, k, p, tries=40, seed=None)
	edges.append(nx.number_of_edges(my_graph))
        avg_sht = nx.average_shortest_path_length(my_graph, weight=None)
        clust = nx.average_clustering(my_graph)
        avg_shortest_path.append(avg_sht)
        cluster_coefficient.append(clust)
        probability.append(p)
        p += 0.01

    new_avg = np.array(avg_shortest_path)
    avg_min = new_avg.min()
    avg_max = new_avg.max()
    avg = (new_avg - avg_min) / (avg_max - avg_min)

    new_cluster = np.array(cluster_coefficient)
    cluster_min = new_cluster.min()
    cluster_max = new_cluster.max()
    normalized_cluster_coefficient = (new_cluster - cluster_min) / (cluster_max - cluster_min)
    # nx.draw(my_graph)
    print edges
    plt.plot(probability, avg)
    plt.plot(probability, normalized_cluster_coefficient)
    plt.xscale('log')
    plt.savefig('wattz-strogatz.png')
    plt.show()
    return avg, normalized_cluster_coefficient


a = watts_strogatz_model(3500, 4, 0.001)

