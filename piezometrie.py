#!/usr/bin/env python3

import jmespath
import requests
import sys
import urllib.parse
import json
import os
import csv

file_path = 'station_piezo.json'

with open(file_path, 'r') as file:
    loaded_list = json.load(file)


API_URL = 'https://hubeau.eaufrance.fr/api/v1/niveaux_nappes/chroniques'
data_all = []

for station in loaded_list:
    params = {'code_bss': station,'date_debut_mesure' : "2023-01-01", 'date_fin_mesure' : "2024-01-01", 'size': 1000 }

    r = requests.get(API_URL + '?' + urllib.parse.urlencode(params))
    if r.status_code == 200:
        data_all.extend(r.json().get("data", []))
    else:
        print(f"Erreur pour la station {station_id}: {response.status_code}")

with open("piezometrie.csv", mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow(["code_bss", "date_mesure", "niveau_nappe_eau", "mode_obtention","statut","qualification", "code_producteur","profondeur_nappe"])
    for item in data_all:
        writer.writerow([
            item.get("code_bss"),
            item.get("date_mesure"),
            item.get("niveau_nappe_eau"),
            item.get("mode_obtention"),
            item.get("statut"),
            item.get("qualification"),
            item.get("code_producteur"),
            item.get("profondeur_nappe")
        ])