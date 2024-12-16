#!/usr/bin/env python3

import jmespath
import requests
import sys
import urllib.parse
import json
import os
import csv
import pandas as pd


API_URL = "https://hubeau.eaufrance.fr/api/v1/niveaux_nappes/stations?code_departement=75%2C77%2C78%2C91%2C92%2C93%2C94%2C95&date_recherche=2014-01-01&format=json&size=20000"

r = requests.get(API_URL)
data = r.json()

df_communes = pd.read_csv('./data_cleaned/communes_IDF.csv')

communes = df_communes['code_commune'].astype(str).tolist()

results = []
with open("./data_cleaned/stations_piezo.csv", mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow(["code_bss","code_commune_insee"])

    for station in jmespath.search('data[*]', data):
        c = jmespath.search('code_bss', station)
        commune= jmespath.search('code_commune_insee', station)
        if commune in communes : 
            writer.writerow([
                c,
                commune,
            ])
            results.append(c)

file_path = './data_API/station_piezo.json'

with open(file_path, 'w') as file:
    json.dump(results, file)