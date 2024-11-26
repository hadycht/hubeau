#!/usr/bin/env python3

import jmespath
import requests
import sys
import urllib.parse
import json
import os
import csv


API_URL = "https://hubeau.eaufrance.fr/api/v1/niveaux_nappes/stations?code_departement=75,77,78,91,92,93,94,95&format=json&page=1&size=10000"

r = requests.get(API_URL)
data = r.json()

results = []
with open("stations_piezo.csv", mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow(["code_bss","x", "y"])

    for station in jmespath.search('data[*]', data):
        c = jmespath.search('code_bss', station)
        x = jmespath.search('x', station)
        y = jmespath.search('y', station)
        writer.writerow([
            c,
            x,
            y,
        ])
        results.append(c)


file_path = 'station_piezo.json'


with open(file_path, 'w') as file:
    json.dump(results, file)