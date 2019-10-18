import nltk
import numpy as np
import pandas as pd
import tqdm

import networkx as nx


def generate_affiliation_coaffiliation(auteurs_csv_path = "data/Liste_Auteurs_affiliation_photo.csv"):

    try:
        all_auteurs = pd.read_csv(auteurs_csv_path, sep=";")
    except e:
        print(f"unrecognized path, '{auteurs_csv_path}' does not exist")
        exit(-1)
    selected_auteurs = all_auteurs.dropna()

    auteurs = selected_auteurs['Authors_Name']
    affiliations = selected_auteurs['Affiliation']
    unique_affiliation = affiliations.unique()
    auteurs_affiliation = pd.DataFrame(columns = unique_affiliation)
    auteurs_affiliation = pd.DataFrame(np.zeros((len(selected_auteurs),len(unique_affiliation))),columns = unique_affiliation)

    print("calculating affiliations")
    for i, auth in enumerate(selected_auteurs.iterrows()):
        #print(f"{auth[1].Authors_Name}'s authors has {auth[1].Affiliation} aff ")
        auteurs_affiliation.ix[i, auth[1].Affiliation] = 1
        auteurs_affiliation = auteurs_affiliation.rename(index={i: auth[1].Authors_Name})

    print("Saving result of affiliation matrix as auteurs_affiliation.csv")

    auteurs_affiliation.to_csv("data/results/auteur_affiliation.csv")

    co_affiliation = auteurs_affiliation.dot(auteurs_affiliation.T)

    co_affiliation.to_csv("data/results/co_affiliation.csv")
    return co_affiliation

if __name__ == "__main__":
    co_affiliation = generate_affiliation_coaffiliation()

    generate_graph(co_affiliation)