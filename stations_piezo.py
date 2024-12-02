#!/usr/bin/env python3

import jmespath
import requests
import sys
import urllib.parse
import json
import os
import csv


API_URL = "https://hubeau.eaufrance.fr/api/v1/niveaux_nappes/stations?code_departement=75%2C77%2C78%2C91%2C92%2C93%2C94%2C95&date_recherche=2014-01-01&format=json&size=20000"

r = requests.get(API_URL)
data = r.json()

results = []
with open("stations_piezo.csv", mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow(["code_bss","bss_id","longitude", "latitude","code_commune_insee","code_departement"])

    for station in jmespath.search('data[*]', data):
        c = jmespath.search('code_bss', station)
        b = jmespath.search('bss_id', station)
        x = jmespath.search('x', station)
        y = jmespath.search('y', station)
        commune= jmespath.search('code_commune_insee', station)
        departement = jmespath.search('code_departement', station)

        writer.writerow([
            c,
            b,
            x,
            y,
            commune,
            departement,
        ])
        results.append(c)

file_path = 'station_piezo.json'

with open(file_path, 'w') as file:
    json.dump(results, file)