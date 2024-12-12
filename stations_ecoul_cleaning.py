import pandas as pd 
import numpy as np

df_stations = pd.read_csv('data_API/stations_ecoul_idf.csv', sep=';') 

relevant_columns = ['code_station', 'libelle_station', 'code_commune', 'code_departement', 'code_cours_eau', 'libelle_cours_eau','date_maj_station']
df_stations_cleaned = df_stations[relevant_columns]

df_stations_cleaned.dropna(subset=['libelle_station'], inplace=True)
df_stations_cleaned.info()


df_stations_cleaned.to_csv('data_cleaned/stations_ecoul_idf.csv', sep=',', index=False)
