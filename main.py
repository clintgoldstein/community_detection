import fileinput
import networkx as nx
import matplotlib.pyplot as plt

#functions
def calc_quality(Graph):
	comminity_edges=0
	for x in range(0, (G.number_of_nodes()-1)):
		for y in range(1-G.number_of_nodes()):
				if G.has_edge(x, y):
					print x
					print y
		
	
	
	
	
#------------------------begin main--------------------------	

# create graph object
G=nx.Graph()

# open file and fill graph
infile= open("karate.txt", "r")
for line in infile:
	nodes=line.split()
	G.add_edge(int(nodes[0]), int(nodes[1]))

#put each node in its own community	
for node in G:
	G.node[node]['group']=node
	

#run initial quality check
calc_quality(G)




#------------------------debug stuff------------------------
print(list(G.nodes(data=True)))
print " "
print(list(G.edges()))
nx.draw(G)
plt.show()