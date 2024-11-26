#!/usr/bin/env python3

import jmespath
import requests
import sys
import urllib.parse
import json
import os
import csv

file_path = 'station_qualite.json'

with open(file_path, 'r') as file:
    loaded_list = json.load(file)


API_URL = 'https://hubeau.eaufrance.fr/api/v1/qualite_nappes/analyses'
data_all = []
results = []

for station in loaded_list:
    params = {'bss_id': station,'date_debut_prelevement' : "2023-01-01", 'date_fin_prelevement' : "2024-01-01", 'size': 20000 }

    r = requests.get(API_URL + '?' + urllib.parse.urlencode(params))
    if r.status_code == 200:
        data_all.extend(r.json().get("data", []))
    else:
        print(f"Erreur pour la station {station_id}: {response.status_code}")

with open("qualite_nappe.csv", mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow(["bss_id", "date_debut_prelevement", "longitude", "latitude", "altitude","nom_bassin_dce","code_bassin_dce", "nom_commune_actuel", "code_insee_actuel","nom_departement", "num_departement", "code_param","nom_param", "resultat","code_unite", "nom_unite"])
    for item in data_all:
        writer.writerow([
            item.get("bss_id"),
            item.get("date_debut_prelevement"),
            item.get("longitude"),
            item.get("latitude"),
            item.get("altitude"),
            item.get("nom_bassin_dce"),
            item.get("code_bassin_dce"),
            item.get("nom_commune_actuel"),
            item.get("code_insee_actuel"),
            item.get("nom_departement"),
            item.get("num_departement"),
            item.get("code_param"),
            item.get("nom_param"),
            item.get("resultat"),
            item.get("code_unite"),
            item.get("nom_unite"),
        ])
