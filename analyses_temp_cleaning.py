import pandas as pd 

df_analyses = pd.read_csv('./data_API/analyses_temp.csv', sep=';')

relevant_columns = ['code_station', 'code_parametre', 'libelle_parametre', 'resultat', 'code_unite', 'libelle_unite']