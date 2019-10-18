#sys imports

import os

#lib imports
import Cluster_Ensembles as CE
import numpy as np
#project related imports
from src import generate_affiliation_coaffiliation, generate_document_auteurs, generate_doc_terms, generate_graph

def main():
    if not os.path.isdir("data/results"):
        os.makedirs("data/results")

    print("generating co affiliation matrix and graph")
    co_affiliation = generate_affiliation_coaffiliation("co_affiliation")

    generate_graph(co_affiliation)

    print("generating documents auteurs matrix")
    generate_document_auteurs()

    print("generating doc term matrix")
    generate_doc_terms()

    print("done")

    print("Using all values")

    c_1 = np.genfromtxt('data/results/partition_co_affiliation.csv', delimiter=',')
    c_2 = np.genfromtxt('data/results/partition_co_term.csv', delimiter=',')
    c_3 = np.genfromtxt('data/results/partition_co_auteur.csv', delimiter=',')
    cluster_run = np.array([c_1, c_2, c_3])
    consensus_labels = CE.cluster_ensembles(cluster_run, N_clusters_max = 10)

    

    np.savetxt("data/results/consensus.csv", consensus_labels, delimiter = ";")

if __name__ == "__main__":

    main()