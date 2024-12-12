#!/usr/bin/env python3

import jmespath
import requests
import sys
import urllib.parse
import json
import os
import csv

file_path = './data_API/station_piezo.json'

with open(file_path, 'r') as file:
    loaded_list = json.load(file)


API_URL = 'https://hubeau.eaufrance.fr/api/v1/niveaux_nappes/chroniques'
data_all = []

for station in loaded_list:
    params = {'code_bss': station,'date_debut_mesure' : "2014-01-01", 'size': 20000 }

    r = requests.get(API_URL + '?' + urllib.parse.urlencode(params))
    if r.status_code in  [200, 206]:
        data_all.extend(r.json().get("data", []))
    else:
        print(f"Erreur pour la station {station}: {r.status_code}")

file_path = './data_API/data_piezo.json'

with open(file_path, 'w') as file:
    json.dump(data_all, file)


