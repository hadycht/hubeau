import pandas as pd

data = pd.read_csv('qualite_nappe.csv', sep=';')

data["date_debut_prelevement"] = data["date_debut_prelevement"].str[:4]
data["code_unite"] = data["code_unite"].fillna(-1).astype(int)

resultats = data.groupby(['bss_id', 'date_debut_prelevement','code_param']).agg(
    nom_bassin_dce=("nom_bassin_dce", "first"),
    code_bassin_dce=("code_bassin_dce", "first"),
    nom_param = ("nom_param", "first"),
    resultat =  ("resultat", "mean"),
    code_unite = ("code_unite", "first"),
    nom_unite = ("nom_unite", "first"),
).reset_index()


#resultats = pd.merge(resultats, resultats, on=['bss_id','date_debut_prelevement'])
resultats.to_csv("resultat_qualite.csv",sep=';', index=False)