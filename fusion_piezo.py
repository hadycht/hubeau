import pandas as pd

piezometrie = pd.read_csv('piezometrie.csv', sep=';')
stations = pd.read_csv('stations_piezo.csv', sep=';')

list_bss = piezometrie['code_bss']
resultats = piezometrie.groupby("code_bss").agg(
    niveau_nappe_eau=("niveau_nappe_eau", "mean"),
    profondeur_nappe=("profondeur_nappe", "mean"),
    mode_obtention=("mode_obtention", "first"),
    statut=("statut", "first"),
    qualification = ("qualification", "first"),
    code_producteur =  ("code_producteur", "first"),
).reset_index()



resultats = pd.merge(resultats, stations, on='code_bss', how='left')
resultats.to_csv("resultats_piezo.csv",sep=';', index=False)
