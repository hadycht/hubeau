#!/usr/bin/env python3

import jmespath
import requests
import sys
import urllib.parse
import json
import os
import csv


API_URL = "https://hubeau.eaufrance.fr/api/v1/qualite_nappes/stations"

#params = {'size': 20000 }

#r = requests.get(API_URL + '?' + urllib.parse.urlencode(params))

#data = r.json()

results = []
#list_departement = []
#for station in jmespath.search('data[*]', data):
#       c = jmespath.search('num_departement', station)
#        if c is not None:
#                list_departement.append(c)

#list_departement = list(set(list_departement))

list_departement = [75,77,78,91,92,93,94,95]

with open("./data_cleaned/stations_qualite_nappes.csv", mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(["bss_id","code_commune_insee"])

        for departement in list_departement:
                params = {'num_departement' : departement, 'size': 20000 }
                r = requests.get(API_URL + '?' + urllib.parse.urlencode(params))

                data = r.json()

                for station in jmespath.search('data[*]', data):
                        d = jmespath.search('bss_id', station)
                        if d is not None:
                                results.append(d)

                        commune= jmespath.search('code_insee', station)


                        writer.writerow([
                                d,
                                commune,
                        ])

file_path = './data_API/station_qualite_nappes.json'

with open(file_path, 'w') as file:
    json.dump(results, file)