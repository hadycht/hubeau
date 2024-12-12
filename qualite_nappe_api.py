#!/usr/bin/env python3

import jmespath
import requests
import sys
import urllib.parse
import json
import os
import csv
import pandas as pd

file_path = './data_API/station_qualite_nappes.json'

with open(file_path, 'r') as file:
    loaded_list = json.load(file)


API_URL = 'https://hubeau.eaufrance.fr/api/v1/qualite_nappes/analyses'
data_all = []
results = []
list_param = "1295,1301,1302,1303,1311,1312,1313,1314,1335,1340,1369,1382,1383,1387,1388,1392,1433,1449,1450"

non_empty_station = []

for i,station in enumerate(loaded_list):
    params = {'bss_id': station, 'code_param' : list_param,'date_debut_prelevement' : "2014-01-01", 'size': 20000}

    r = requests.get(API_URL + '?' + urllib.parse.urlencode(params))
    if r.status_code in  [200, 206]:
        data = r.json().get("data", [])
        if data:
            data_all.extend(data)
            non_empty_station.append(i)
    else:
        print(f"Erreur pour la station {station}: {r.status_code}")

file_path = "./data_cleaned/stations_qualite_nappes.csv"
df = pd.read_csv(file_path)

filtered_df = df.iloc[non_empty_station]

filtered_df.to_csv("./data_cleaned/stations_qualite_nappes.csv", index=False)

file_path = './data_API/data_qualite_nappes.json'

with open(file_path, 'w') as file:
    json.dump(data_all, file)
