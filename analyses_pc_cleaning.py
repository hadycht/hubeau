import pandas as pd 

df_analyses = pd.read_csv('./data_API/analyses_pc.csv', sep=';')
# print("initial shape ", df_analyses.shape)
# print(df_analyses.info())

df_stations = pd.read_csv('./data_cleaned/stations_pc_idf.csv')
df_analyses = df_analyses[df_analyses['code_station'].isin(df_stations['code_station'])]

#drop rows with nan values in resultat (they represent 1% of the dataset)

df_analyses = df_analyses.dropna(subset=['resultat'])
# print(df_analyses.info())

# faire une sorte d'avoir une seule mesure par data pour chaque station
result = df_analyses.groupby(['date_prelevement','code_station', 'code_parametre'], as_index=False).agg({
    'libelle_parametre': 'first',
    'resultat': 'mean', 
    'code_unite': 'first',
    'symbole_unite': 'first'
})

# print("after cleaning shape ", result.shape)
result.to_csv('data_cleaned/analyses_pc.csv', sep=',', index=False)