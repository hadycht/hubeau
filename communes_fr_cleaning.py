import pandas as pd 

df_communes = pd.read_csv('data_API/communes_fr.csv', sep=';')

# print(df_communes.columns)
relevant_columns = ['CdCommune', 'LbCommune', 'CdRegion', 'LbRegion',
       'CdDepartement', 'LbDepartement', 'CdBassinDCE', 'NomBassinDCE']

df_communes_cleaned = df_communes[relevant_columns]

df_communes_idf = df_communes_cleaned[df_communes_cleaned['CdRegion'] == 11].copy()

df_communes_idf.drop(['CdRegion', 'LbRegion'], axis=1, inplace=True)

renaming_relevant_columns = {
    'CdCommune' : 'code_commune', 
    'LbCommune' : 'libelle_commune', 
    'CdDepartement' : 'code_departement', 
    'LbDepartement' : 'libelle_departement', 
    'CdBassinDCE' : 'code_bassin_DCE', 
    'NomBassinDCE' : 'libelle_bassin_DCE'
}

df_communes_idf.rename(columns=renaming_relevant_columns, inplace=True)
df_communes_idf.to_csv('data_cleaned/communes_IDF.csv', sep=',', encoding='UTF8', index=None)

