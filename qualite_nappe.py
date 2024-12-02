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
list_param = "1295,1301,1302,1303,1311,1312,1313,1335,1337,1338,1340,1369,1382,1383,1387,1392,1433,1449,1450"

for station in loaded_list:
    params = {'bss_id': station, 'code_param' : list_param,'date_debut_prelevement' : "2013-01-01", 'size': 20000}

    r = requests.get(API_URL + '?' + urllib.parse.urlencode(params))
    if r.status_code in  [200, 206]:
        data_all.extend(r.json().get("data", []))
    else:
        print(f"Erreur pour la station {station}: {r.status_code}")

file_path = 'data_qualite.json'

with open(file_path, 'w') as file:
    json.dump(data_all, file)
