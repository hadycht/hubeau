import pandas as pd 

df = pd.read_csv("./data_API/analyses_eau_pot.csv", delimiter=';') 

df = df.dropna(subset=['resultat_numerique'])
df['resultat_numerique'] = df['resultat_numerique'].round(2)

df['date_prelevement'] = df['date_prelevement'].apply(lambda x : x.split('T')[0])

print(df.head(5))
print(df.shape)
print(df.info())

# faire une sorte d'avoir une seule mesure par data pour chaque station
result = df.groupby(['date_prelevement','code_commune', 'code_parametre'], as_index=False).agg({
    'libelle_parametre': 'first',
    'resultat_numerique': 'mean', 
    'libelle_unite': 'first',
    'nom_commune' : 'first'
})

print("after cleaning shape ", result.shape)
result.to_csv('data_cleaned/analyses_eau_potable.csv', sep=',', index=False)
