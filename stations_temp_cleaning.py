import pandas as pd 
import numpy as np

df_stations = pd.read_csv('data_API/stations_temp.csv', sep=';') 

relevant_columns = ['code_station', 'libelle_station', 'code_commune', 'code_cours_eau', 'libelle_cours_eau','date_maj_infos']
df_stations_cleaned = df_stations[relevant_columns]

df_stations_cleaned.dropna(subset=['code_commune'], inplace=True)

df_stations_cleaned['libelle_cours_eau'] = df_stations_cleaned['libelle_cours_eau'].fillna(df_stations_cleaned['code_cours_eau'])

#df_stations_cleaned.dropna(subset=['code_cours_eau'], inplace=True)

print(df_stations_cleaned.info())

df_stations_cleaned.to_csv('data_cleaned/stations_temp.csv', sep=',', index=False)
