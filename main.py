#sys imports

import os

#lib imports
import pandas as pd
import Cluster_Ensembles as CE
import numpy as np
#project related imports
from src import generate_affiliation_coaffiliation, generate_document_auteurs, generate_doc_terms, generate_graph, reorganise_graph_from_consensus

def main():
    if not os.path.isdir("data/results"):
        os.makedirs("data/results")

    print("generating co affiliation matrix and graph")
    #co_affiliation = generate_affiliation_coaffiliation()
    co_affiliation = pd.read_hdf("data/results/co_affiliation.hdf")
    print(co_affiliation).shape
    #generate_graph(numpy_matrix = co_affiliation.to_numpy(), partition_name = "co_affiliation")

    # print("generating documents auteurs matrix")
    # generate_document_auteurs()

    # print("generating doc term matrix")
    # generate_doc_terms()

    # print("done")

    # print("Using all values")

    c_1 = np.genfromtxt('data/results/partition_co_affiliation.csv', delimiter=',')
    c_2 = np.genfromtxt('data/results/partition_co_term.csv', delimiter=',')
    c_3 = np.genfromtxt('data/results/partition_co_auteur.csv', delimiter=',')
    cluster_run = np.array([c_1, c_2, c_3])
    consensus_labels = CE.cluster_ensembles(cluster_run, N_clusters_max = 10)

    # np.savetxt("data/results/consensus.csv", consensus_labels, delimiter = ";")
    consensus_labels = np.genfromtxt("data/results/consensus.csv", delimiter = ";")
    consensus_labels = consensus_labels.astype(int)
    reorganise_graph_from_consensus(numpy_matrix = co_affiliation.to_numpy(), partition_name = "co_affiliation", consensus= consensus_labels)


if __name__ == "__main__":

    main()
    