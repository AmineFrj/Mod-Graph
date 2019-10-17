import nltk
import numpy as np
import pandas as pd
import tqdm
try:
	all_auteurs = pd.read_csv("Liste_Auteurs_affiliation_photo.csv", sep=";")
except e:
	print("Le csv doit s'appeler : 'Liste_Auteurs_affiliation_photo.csv'")
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

auteurs_affiliation.to_csv("auteur_affiliation.csv")

co_affiliation = auteurs_affiliation.dot(auteurs_affiliation.T)

co_affiliation.to_csv("co_affiliation.csv")