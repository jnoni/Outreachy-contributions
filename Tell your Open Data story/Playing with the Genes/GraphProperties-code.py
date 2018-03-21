import networkx as nx
#import matplotlib.pyplot as plt
import numpy as np
#import matplotlib.colors as mcolors
#import community.community_louvain as community
import random
import operator
from collections import defaultdict

# uncomment and run functions one by one in under "if __name__ == "main" "

def create_network(G,filename):
	G = nx.read_edgelist(filename)
	print nx.number_of_nodes(G)
	print nx.number_of_edges(G)
	return G

def degree_distribution(G):
	degrees = G.degree()
	values = sorted(set(degrees.values())) 
	hist = [degrees.values().count(x) for x in values]
	plt.figure()
	plt.title("Degree Distribution")
	plt.ylabel("Number Of Nodes")
	plt.xlabel("Number Of Links")
	plt.plot(values,hist,'ro-')
	plt.savefig('degree_distribution.png')
	plt.show()
	

def log_scale_degree_distribution(G):
	plt.figure()
	degree_sequence=sorted(nx.degree(G).values(),reverse=True) # degree sequence
	#print "Degree sequence", degree_sequence
	dmax=max(degree_sequence)

	plt.loglog(degree_sequence,'b-',marker='o')
	plt.title("Network")
	plt.ylabel("degree")
	plt.xlabel("log_scale")
	plt.savefig('log_scale_graph.png')
	plt.close()
	# draw graph in inset
	#plt.axes([0.45,0.45,0.45,0.45])

def modularity():
	return 1

def print_topological_features(G):
	Gc = max(nx.connected_component_subgraphs(G), key=len)
	#print nx.average_clustering(Gc)
	#print nx.average_shortest_path_length(Gc)
	return Gc

def plot_network(G):
	plt.figure()
	degree_sequence=sorted(nx.degree(G).values(),reverse=True) # degree sequence
	dmax=max(degree_sequence)
	plt.title("Network")
	Gcc=sorted(nx.connected_component_subgraphs(G), key = len, reverse=True)[0]
	n = nx.	number_of_nodes(Gcc)
	d = nx.degree(Gcc)
	nx.draw(Gcc, nodelist=d.keys(), node_size=[v * 2 for v in d.values()],cmap='viridis')
	plt.axis('off')	
	plt.savefig('network.png')
	plt.show()

def plot_graph(G):
	ncols = 56
	print G.nodes()
	degree_sequence=sorted(nx.degree(G).values(),reverse=True)
	print degree_sequence
	fig, ax = plt.subplots()
	num_nodes = range(nx.number_of_nodes(G))
	keys = G.nodes()
	n = nx.number_of_nodes(G)
	pos = {keys[i] : (i % ncols, (n-i-1)//ncols) for i in num_nodes}
	#print pos,len(pos)
	fig, ax = plt.subplots()
	#plt.axes([0.45,0.45,0.45,0.45])
	degrees = G.degree()
	nodes = G.nodes()
	n_color = np.asarray([degrees[n] for n in nodes])
	sc = nx.draw_networkx_nodes(G,  pos = pos,nodelist=nodes, node_color=n_color, cmap='viridis',
                            with_labels=False, ax=ax,node_size=n_color)
	fig.colorbar(sc)
	sc.set_norm(mcolors.LogNorm())
	#plt.show(fig)
	fig.savefig('graph_figure.png')
	plt.close(fig)

def detect_community(G):
	plt.figure()
	part = community.best_partition(G)
	#print part
	mod = community.modularity(part,G)
	print("modularity:", mod)
	reversed_dict = defaultdict(list)
	for key,value in part.iteritems():
    		reversed_dict[value].append(str(key))
	print reversed_dict
	for (item, nodes) in reversed_dict.iteritems():
		with open('modules.txt', "a") as f:
			print ('Module %s Nodes %s' % (item, nodes))
        		f.write(str(item))
        		f.write(str(nodes))
			f.write('\n')
	f.close()
	#values1 = set(a for b in part.values() for a in b)
	#reverse_d = dict((new_key, [key for key,value in part.items() if new_key in value]) for new_key in values1)
	#print reverse_d
	#print part
	values = [part.get(node) for node in G.nodes()]
	#print values
	#nx.draw_graphviz(G,cmap = plt.get_cmap('jet'), node_color = values, node_size=30, with_labels=False)
	nx.draw_spring(G, cmap = plt.get_cmap('jet'), node_color = values, node_size=30, with_labels=False)
	plt.savefig('detect_community.png')
	plt.show()


def plotGraph_GiantCluster(GC_Size,fraction_nodes):
	plt.title('Random node deletion')
	plt.xlabel('fraction of nodes')
	plt.ylabel('Giant cluster size')
	plt.plot(fraction_nodes,GC_Size, marker='o', color='b')
	plt.savefig('GiantCluster3_targetted.png')
	plt.show()
	plt.close()

def plotGraph_isolated(Subgraph_size,fraction_nodes):
	plt.title('Random node deletion')
	plt.xlabel('fraction of nodes')
	plt.ylabel('isolated nodes size')
	plt.plot(fraction_nodes,Subgraph_size, marker='o', color='b')
	plt.savefig('Graph_isolated3_targetted.png')
	plt.show()
	plt.close()

def remove_fraction(G,fraction):
	cpl = 0
	n = nx.number_of_nodes(G)
	nodes_deleted = fraction * n
	while(nodes_deleted>0):
		node = random.choice(G.nodes())
		#print node,nodes_deleted
		G.remove_node(node)
		nodes_deleted=nodes_deleted - 1
	
	graphs = list(nx.connected_component_subgraphs(G))
	#graphs.remove(max(graphs))
	sub_graphs = [nx.number_of_nodes(i) for i in graphs]
	subgraph_size =0
	if(len(sub_graphs)!=0):
		subgraph_size = sum(sub_graphs)/float(len(sub_graphs))
	else:
		subgraph_size = 1
	largest_cc = max(nx.connected_component_subgraphs(G), key=len)
	cpl = nx.average_shortest_path_length(largest_cc)
	gc_size = nx.number_of_nodes(largest_cc)/float(n)
	print cpl
	return G,cpl,gc_size,subgraph_size

def SF_random_failure(G):
	GC_Size = []
	GC_Size.append(1)
	cpl = []
	cpl.append(nx.average_shortest_path_length(G))
	Subgraph_size = []
	Subgraph_size.append(1)
	fraction_nodes = []
	fraction_nodes.append(0)
	#t1 = np.arange(0.0, 0.4, 0.01)
	fraction = 0.001
	while(fraction<=0.04):
		G,cpl_new,gc_size,subgraph_size =remove_fraction(G,0.001) 
		cpl.append(cpl_new)
		GC_Size.append(float(gc_size))
		Subgraph_size.append(subgraph_size)
		fraction = fraction + 0.001
		fraction_nodes.append(fraction)
	#plt.figure()
	plt.title('random node deletion')
	plt.xlabel('fraction of nodes')
	plt.ylabel('characteristic path length')
	plt.plot(fraction_nodes,cpl, linestyle='--',marker='o', color='b')
	plt.savefig('SFNodeDeletion1_cpl_random(4).png')
	plt.show()
	plt.close()
	plotGraph_GiantCluster(GC_Size,fraction_nodes)
	plotGraph_isolated(Subgraph_size,fraction_nodes)

def remove_nodes2(G,fraction):
	cpl = 0
	n = nx.number_of_nodes(G)
	degree_nodes = G.degree()
	nodes_degree_list = sorted(degree_nodes.items(), key=operator.itemgetter(1),reverse=True)
	#print nodes_degree_list
	nodes_deleted = int(fraction * n)
	for i in range(nodes_deleted):
		G.remove_node(nodes_degree_list[i][0])

	graphs = list(nx.connected_component_subgraphs(G))
	#graphs.remove(max(graphs))
	sub_graphs = [nx.number_of_nodes(i) for i in graphs]
	subgraph_size =0
	if(len(sub_graphs)!=0):
		subgraph_size = sum(sub_graphs)/float(len(sub_graphs))
	else:
		subgraph_size = 1
	largest_cc = max(nx.connected_component_subgraphs(G), key=len)
	cpl = nx.average_shortest_path_length(largest_cc)
	gc_size = nx.number_of_nodes(largest_cc)/float(n)
	print cpl
	return G,cpl,gc_size,subgraph_size

def some_other_top_features(G):
	r=nx.degree_assortativity_coefficient(G)
	print "degree correlation coefficient",r

def average_degree_connectivityPlots(G):
	avg_degree_conn = nx.average_degree_connectivity(G)
	hist = [i for i in avg_degree_conn.keys()]
	values = [i for i in avg_degree_conn.values()]
	plt.figure()
	plt.xlabel('degree')
	plt.ylabel('average connectivity')
	plt.plot(hist,values,'ro')
	plt.savefig('avg_deg_connectivity')
	plt.close()

def betweenness_centrality_graph(G):
	avg_degree_conn = nx.betweenness_centrality(G)
	hist = [i for i in avg_degree_conn.keys()]
	values = [i for i in avg_degree_conn.values()]
	plt.figure()
	plt.xlabel('node')
	plt.ylabel('betweenness centrality')
	plt.plot(hist,values,'ro')
	plt.savefig('betweenness centrality')
	plt.close()

def closeness_centrality_graph(G):
	avg_degree_conn = nx.closeness_centrality(G)
	hist = [i for i in avg_degree_conn.keys()]
	values = [i for i in avg_degree_conn.values()]
	plt.figure()
	plt.xlabel('node')
	plt.ylabel('closeness centrality')
	plt.plot(hist,values,'ro')
	plt.savefig('closeness centrality')
	plt.close()

def node_deletion_targeted(G):
	cpl = []
	GC_Size = []
	GC_Size.append(1)
	Subgraph_size = []
	Subgraph_size.append(1)
	cpl.append(nx.average_shortest_path_length(G))
	fraction_nodes = []
	fraction_nodes.append(0)
	fraction = 0.001
	while(fraction<=0.04):
		G,cpl_new,gc_size,subgraph_size = remove_nodes2(G,0.001)
		cpl.append(cpl_new)
		GC_Size.append(float(gc_size))
		Subgraph_size.append(subgraph_size)
		fraction = fraction + 0.001
		fraction_nodes.append(fraction)
	#plt.figure()
	plt.title('Targetted node deletion')
	plt.xlabel('fraction of nodes')
	plt.ylabel('characteristic path length')
	plt.plot(fraction_nodes,cpl,  linestyle='--',marker='o', color='b')
	plt.savefig('SFNodeDeletion_cpl_targetted(4).png')
	plt.show()
	plt.close()
	plotGraph_GiantCluster(GC_Size,fraction_nodes)
	plotGraph_isolated(Subgraph_size,fraction_nodes)
	
def identify_hubs(G):
	degree_nodes = G.degree()
	nodes_degree_list = sorted(degree_nodes.items(), key=operator.itemgetter(1),reverse=True)
	#print nodes_degree_list
	print nodes_degree_list[:10]
if __name__ == "__main__":
	G = nx.Graph()
	G=create_network(G,'mygraph.edgelist')
	#G = print_topological_features(G)
	identify_hubs(G)
	#SF_random_failure(G)
	#node_deletion_targeted(G)
	#degree_distribution(G)
	#detect_community(G)
	#degree_distribution(G)
	#plot_graph(G)
	#plot_network(G)
	#some_other_top_features(G)
	#average_degree_connectivityPlots(G)
	#betweenness_centrality_graph(G)
	#closeness_centrality_graph(G)
	
	
	
