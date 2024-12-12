import requests
import sys
import urllib.parse
import json
import os
import csv
import pandas as pd

file_path = './data_API/data_piezo.json'
with open(file_path, 'r') as file:
    data = json.load(file)


with open("./data_cleaned/piezometrie.csv", mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow(["code_bss", "date_mesure", "profondeur_nappe", "niveau_nappe_eau"])
    for item in data:
        writer.writerow([
            item.get("code_bss"),
            item.get("date_mesure"),
            item.get("profondeur_nappe"),
            item.get("niveau_nappe_eau"),
        ])