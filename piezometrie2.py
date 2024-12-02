import requests
import sys
import urllib.parse
import json
import os
import csv
import pandas as pd

file_path = 'data_piezo.json'
with open(file_path, 'r') as file:
    data = json.load(file)


with open("piezometrie.csv", mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow(["code_bss", "date_mesure", "profondeur_nappe", "niveau_nappe_eau", "mode_obtention","statut","qualification", "code_producteur"])
    for item in data:
        writer.writerow([
            item.get("code_bss"),
            item.get("date_mesure"),
            item.get("profondeur_nappe"),
            item.get("niveau_nappe_eau"),
            item.get("mode_obtention"),
            item.get("statut"),
            item.get("qualification"),
            item.get("code_producteur"),
        ])

piezometrie = pd.read_csv('piezometrie.csv', sep=';')
stations = pd.read_csv('stations_piezo.csv', sep=';')


resultats = pd.merge(piezometrie, stations, on='code_bss', how='left')
resultats.to_csv("resultats_piezo.csv",sep=';', index=False)