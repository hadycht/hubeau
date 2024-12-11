import pandas as pd 
import numpy as np

df_stations = pd.read_csv('data_API/stations_pc_idf.csv', sep=';') 

relevant_columns = ['code_station', 'libelle_station', 'code_commune', 'code_departement', 'code_cours_eau', 'nom_cours_eau','date_creation','date_arret','date_maj_information']
df_stations_cleaned = df_stations[relevant_columns]

# Some stations don't have the 'cours d eau' associated to it, 
# so we assign to it one randomly from the its commune, and if nothing in commune, we check its departement

# function to handle NaN replacement within each group
def replace_nan_with_random(group):
    valid_pairs = group[['code_cours_eau', 'nom_cours_eau']].dropna().drop_duplicates().values

    if len(valid_pairs) > 0:
        group[['code_cours_eau', 'nom_cours_eau']] = group[['code_cours_eau', 'nom_cours_eau']].apply(
            lambda row: valid_pairs[np.random.choice(len(valid_pairs))] if pd.isna(row['code_cours_eau']) else row,
            axis=1,
            result_type='expand'
        )
    return group


# groupby by code_commune
df_cleaned = df_stations_cleaned.groupby('code_commune').apply(replace_nan_with_random)

# groupby by code departement 
df_cleaned_twice = df_stations_cleaned.groupby('code_departement').apply(replace_nan_with_random)

df_cleaned_twice.dropna(subset=['code_cours_eau'],inplace=True) 

df_cleaned_twice.drop('code_departement', axis=1, inplace=True)

df_cleaned_twice.reset_index(drop=True, inplace=True)

print(len(df_cleaned_twice['code_commune'].unique()))
df_cleaned_twice.to_csv('data_cleaned/stations_pc_idf.csv', sep=',', index=False)
