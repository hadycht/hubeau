#!/usr/bin/env python3

import jmespath
import requests
import sys
import urllib.parse
import json
import os
import csv


API_URL = "https://hubeau.eaufrance.fr/api/v1/qualite_nappes/stations?format=json&num_departement=75,77,78,91,92,93,94,95&page=1&size=10000"

r = requests.get(API_URL)
data = r.json()

results = []
for station in jmespath.search('data[*]', data):
        c = jmespath.search('bss_id', station)
        results.append(c)


file_path = 'station_qualite.json'


with open(file_path, 'w') as file:
    json.dump(results, file)