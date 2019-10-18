import networkx as nx
import community
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd 
import random

def generate_graph(df, partition_name, debug = False, verbose = True):
    df = df.to_numpy()
    graph = nx.from_numpy_matrix(df)

    nx.draw(graph)

    plt.title("graphe")
    plt.show()

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
    nx.draw_networkx_edges(graph, pos, alpha=0.5)
    plt.axis("off")
    plt.show()

    #Reorganisation de la matrice
    clustering1 = np.asarray(list(partition.values()))
    index = np.argsort(clustering1)

    partition.values()
    if verbose :
        print("index : ", index)
    df2 = df[index,:]
    df2 = df2[:,index]

    graph2 = nx.from_numpy_matrix(df2)
    partition2 = community.best_partition(graph2)

    # Affichage du graphe
    pos = nx.spring_layout(graph2)
    count = 0
    for com in set(partition2.values()):
        list_nodes = [nodes for nodes in partition2.keys() if partition2[nodes]==com]
        nx.draw_networkx_nodes(graph2,pos,list_nodes,node_size = 20, node_color=colors[count])
        count += 1
    nx.draw_networkx_edges(graph2, pos, alpha=0.5)
    plt.axis("off")
    plt.show()


    np.savetxt(f"data/results/partition_{partition_name}.csv", np.asarray(list(partition.values())))