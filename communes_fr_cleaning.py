import pandas as pd 

df_communes = pd.read_csv('data_API/communes_FR.csv', sep=';')

# print(df_communes.columns)
relevant_columns = ['CdCommune', 'LbCommune', 'CdRegion', 'LbRegion',
       'CdDepartement', 'LbDepartement', 'CdBassinDCE', 'NomBassinDCE']

df_communes_cleaned = df_communes[relevant_columns]

df_communes_cleaned.to_csv('data_cleaned/communes_FR.csv', sep=',', encoding='UTF8', index=None)

# unique_bass = df_communes_cleaned['NomBassinDCE'].unique() 
# unique_bass_1 = df_communes_cleaned['CdBassinDCE'].unique() 
# unique_reg = df_communes_cleaned['LbRegion'].unique()

# print("Unique regions are ", unique_reg,' and their number is ', len(unique_reg))
# print("Unique bassins are ", unique_bass,' and their number is ', len(unique_bass_1))
# print(df_communes_cleaned.shape)
# print(df_communes_cleaned.head(5))
# print(df_communes.head(5))
# print(df_communes.shape)
