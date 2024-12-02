import requests
import sys
import urllib.parse
import json
import os
import csv
import pandas as pd

file_path = 'data_qualite.json'
with open(file_path, 'r') as file:
    data = json.load(file)



with open("qualite_nappe.csv", mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow(["bss_id", "date_debut_prelevement", "nom_bassin_dce","code_bassin_dce",  "code_param","nom_param", "resultat","code_unite", "nom_unite"])
    for item in data:
        writer.writerow([
            item.get("bss_id"),
            item.get("date_debut_prelevement"),
            item.get("nom_bassin_dce"),
            item.get("code_bassin_dce"),
            item.get("code_param"),
            item.get("nom_param"),
            item.get("resultat"),
            item.get("code_unite"),
            item.get("nom_unite"),
        ])
