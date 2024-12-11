import requests
import pandas as pd

def fetch_all_data(url, output_file):

    # Choose the initial day that you want
    initial_date = "2014-01-01"
    size = 20000
    params = {
        "size" : size,
        "date_debut_prelevement" : initial_date,
        "fields" : "code_station,code_parametre,libelle_parametre,resultat,date_prelevement,code_unite,symbole_unite",
        "code_parametre": "1301,1302,1303,1295,1311,1312,1313,1314,1335,1340,1433,1382,1388,1387,1369,1383,1392,1449,1450",
        "code_departement": "75,77,78,91,92,93,94,95"
    }

    response = requests.get(url, params)
    done = True
    if response.status_code not in  [200, 206]:
        done = False
        print(f"Error: {response.status_code} - {response.text}")
        
    with open(output_file, 'wb') as f : 
        f.write(response.content)

    stop = size

    # Dealing with pagination 
    while True:
        # if we retrieve less than the initial size, then we arrived at the end 
        if stop != size : 
            done = True
            break

        with open('temp.csv', 'wb') as f : 
            f.write(response.content)

        df = pd.read_csv('temp.csv', sep=";")
        stop = len(df)
        
        # the dataset is already sorted by date
        last_date = df.tail(1)['date_prelevement'].iloc[0]
        # Convertir en datetime
        last_date = pd.to_datetime(last_date)

        # Ajouter un jour
        next_date = last_date + pd.Timedelta(days=1)

        print(last_date)
        params = {
            "size" : size,
            "date_debut_prelevement" : next_date,
            "fields" : "code_station,code_parametre,libelle_parametre,resultat,date_prelevement,code_unite,symbole_unite",
            "code_parametre": "1301,1302,1303,1295,1311,1312,1313,1314,1335,1340,1433,1382,1388,1387,1369,1383,1392,1449,1450",
            "code_departement": "75,77,78,91,92,93,94,95"
        }
        response = requests.get(url, params)

        if response.status_code not in  [200, 206]:
            done = False
            print(f"Error: {response.status_code} - {response.text}")
            break
        
        #deal with the header
        lines = response.content.splitlines(True)[1:]
        with open(output_file, 'ab') as f : 
            for line in lines : 
                f.write(line)
        
    print("DONE", done)
    return 

url = "https://hubeau.eaufrance.fr/api/v2/qualite_rivieres/analyse_pc.csv"
output_file = "./data_API/analyses_pc.csv"

fetch_all_data(url, output_file)