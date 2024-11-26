import pandas as pd 
import numpy as np

df_stations = pd.read_csv('data_API/stations_pc.csv', sep=';') 

relevant_columns = ['code_station', 'libelle_station', 'code_commune', 'code_departement', 'code_cours_eau', 'nom_cours_eau','date_creation','date_arret','date_maj_information']
df_stations_cleaned = df_stations[relevant_columns]

# Define a function to handle NaN replacement within each group
def replace_nan_with_random(group):
    # Get valid (code_cours_eau, nom_cours_eau) pairs
    valid_pairs = group[['code_cours_eau', 'nom_cours_eau']].dropna().drop_duplicates().values

    # Replace NaN values if there are valid pairs
    if len(valid_pairs) > 0:
        group[['code_cours_eau', 'nom_cours_eau']] = group[['code_cours_eau', 'nom_cours_eau']].apply(
            lambda row: valid_pairs[np.random.choice(len(valid_pairs))] if pd.isna(row['code_cours_eau']) else row,
            axis=1,
            result_type='expand'
        )
    return group


# Group by 'code_commune' and apply the function
df_cleaned = df_stations_cleaned.groupby('code_commune').apply(replace_nan_with_random)

# print(df_cleaned.columns)

# print(df_cleaned.shape)
# print(sum(df_cleaned['code_cours_eau'].isnull()) / df_cleaned.shape[0] * 100)
# print(df_cleaned.head(5))

df_cleaned_twice = df_stations_cleaned.groupby('code_departement').apply(replace_nan_with_random)

# print(df_cleaned_twice.columns)

# print(df_cleaned_twice.shape)
# print(sum(df_cleaned_twice['code_cours_eau'].isnull()) / df_cleaned_twice.shape[0] * 100)
# print(df_cleaned_twice.head(5)) 

df_cleaned_twice.dropna(subset=['code_cours_eau'],inplace=True) 

# print(sum(df_cleaned_twice['code_cours_eau'].isnull()) / df_cleaned_twice.shape[0] * 100)
# print(sum(df_cleaned_twice['date_arret'].isnull()) == df_cleaned_twice.shape[1])
# print(sum(df_cleaned_twice['date_arret'].isnull()))

df_cleaned_twice.drop('code_departement', axis=1, inplace=True)

df_cleaned_twice.reset_index(drop=True, inplace=True)

df_cleaned_twice.to_csv('data_cleaned/stations_pc.csv', sep=',', index=False)
