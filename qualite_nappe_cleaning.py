import requests
import sys
import urllib.parse
import json
import os
import csv
import pandas as pd
import numpy as np


file_path = './data_API/data_qualite_nappes.json'
with open(file_path, 'r') as file:
    data = json.load(file)

with open("./data_API/qualite_nappe.csv", mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow(["bss_id", "date_debut_prelevement", "code_param","nom_param", "resultat","code_unite", "nom_unite"])
    for item in data:
        writer.writerow([
            item.get("bss_id"),
            item.get("date_debut_prelevement"),
            item.get("code_param"),
            item.get("nom_param"),
            item.get("resultat"),
            item.get("code_unite"),
            item.get("nom_unite"),
        ])

data = pd.read_csv('./data_API/qualite_nappe.csv', sep=';')

data = data.dropna()

data["date_debut_prelevement"] = data["date_debut_prelevement"].str[:4]
data["code_unite"] = data["code_unite"].fillna(-1).astype(int)

resultats = data.groupby(['bss_id', 'date_debut_prelevement','code_param']).agg(
    nom_param = ("nom_param", "first"),
    resultat =  ("resultat", "mean"),
    code_unite = ("code_unite", "first"),
    nom_unite = ("nom_unite", "first"),
).reset_index()


#resultats = pd.merge(resultats, resultats, on=['bss_id','date_debut_prelevement'])
resultats.to_csv("./data_cleaned/resultat_qualite.csv",sep=';', index=False)
