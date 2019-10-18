import networkx as nx
import community
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd 
import random

def generate_graph(numpy_matrix, partition_name, debug = False, verbose = True):
    graph = nx.from_numpy_matrix(numpy_matrix)

    # nx.draw(graph)

    # plt.title("graphe")
    # plt.show()

    partition = community.best_partition(graph)
    #print("partition", partition)

    # Calcule de modularité
    modularite_value = community.modularity(partition,graph)
    print("modularity_value", modularite_value)
    # Visu du nombre de communautés retrouvés
    vect_label = set(partition.values())
    print("vect_label", vect_label)

    size = int(len(set(partition.values())))
    if verbose:
        print("size", size)
    # genere un vecteur de couleur
    colors = ["#"+''.join([random.choice('0123456789ABCDEF')for j in range(6)])for i in range(size)]

    # Affichage du graphe
    pos = nx.spring_layout(graph)
    count = 0
    for com in set(partition.values()):
        list_nodes = [nodes for nodes in partition.keys() if partition[nodes]==com]
        nx.draw_networkx_nodes(graph,pos,list_nodes,node_size = 20, node_color=colors[count])
        count += 1
    # nx.draw_networkx_edges(graph, pos, alpha=0.5)
    # plt.axis("off")
    # plt.show()

    #Reorganisation de la matrice
    clustering1 = np.asarray(list(partition.values()))
    print("CLUSTER SHAPE", clustering1.shape)
    index = np.argsort(clustering1)

    partition.values()
    if verbose :
        print("index : ", index)
    numpy_matrix2 = numpy_matrix[index,:]
    numpy_matrix2 = numpy_matrix2[:,index]

    graph2 = nx.from_numpy_matrix(numpy_matrix2)
    partition2 = community.best_partition(graph2)

    # Affichage du graphe
    pos = nx.spring_layout(graph2)
    count = 0
    for com in set(partition2.values()):
        list_nodes = [nodes for nodes in partition2.keys() if partition2[nodes]==com]
        nx.draw_networkx_nodes(graph2,pos,list_nodes,node_size = 20, node_color=colors[count])
        count += 1
    # nx.draw_networkx_edges(graph2, pos, alpha=0.5)
    # plt.axis("off")
    # plt.show()

    print(f"genetating partition of {partition_name}")
    np.savetxt(f"data/results/partition_{partition_name}.csv", np.asarray(list(partition.values())))


def reorganise_graph_from_consensus(numpy_matrix, partition_name, consensus):

    print(f"reorganise {partition_name} from consensus")
    graph = nx.from_numpy_matrix(numpy_matrix) #Co affiliation
    print("consensus shape : ", consensus.shape)
    index = np.argsort(consensus)

    numpy_matrix2 = numpy_matrix[index,:]
    numpy_matrix2 = numpy_matrix2[:,index]
    print(numpy_matrix2.shape, '\n',numpy_matrix.shape)
    graph2 = nx.from_numpy_matrix(numpy_matrix2)

    size = len(np.unique(consensus))
    colors = ["#"+''.join([random.choice('0123456789ABCDEF')for j in range(6)])for i in range(size)]

    # Affichage du graphe
    pos = nx.spring_layout(graph2)
    count = 0
    sumz = 0
    for com in np.unique(consensus):
        list_nodes = [node for node in consensus if consensus[node]==com]
        print(f"community {com} has {len(list_nodes)} elements")
        nx.draw_networkx_nodes(graph2,pos,list_nodes,node_size = 2, node_color=colors[count])
        count += 1
        sumz += len(list_nodes)
    print(sumz)
    nx.draw_networkx_edges(graph2, pos, alpha=0.5)
    plt.axis("off")
    plt.show()

