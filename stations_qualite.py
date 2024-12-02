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

with open("stations_qualite.csv", mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(["code_bss","bss_id","longitude", "latitude","altitude","code_commune_insee","nom_commune", "code_departement", "nom_departement","nom_region"])

        for departement in list_departement:
                params = {'num_departement' : departement, 'size': 20000 }
                r = requests.get(API_URL + '?' + urllib.parse.urlencode(params))

                data = r.json()

                for station in jmespath.search('data[*]', data):
                        d = jmespath.search('bss_id', station)
                        if d is not None:
                                results.append(d)
                        c = jmespath.search('code_bss', station)
                        x = jmespath.search('longitude', station)
                        y = jmespath.search('latitude', station)
                        z = jmespath.search('altitude', station)
                        commune= jmespath.search('code_insee', station)
                        n_commune = jmespath.search('nom_commune', station)
                        departement = jmespath.search('num_departement', station)
                        nom_departement = jmespath.search('nom_departement', station)
                        nom_region = jmespath.search('nom_region', station)

                        writer.writerow([
                                c,
                                d,
                                x,
                                y,
                                z,
                                commune,
                                n_commune,
                                departement,
                                nom_departement,
                                nom_region,
                        ])

file_path = 'station_qualite.json'

with open(file_path, 'w') as file:
    json.dump(results, file)