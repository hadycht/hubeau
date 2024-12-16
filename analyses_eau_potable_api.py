import requests
import pandas as pd
from io import StringIO

def fetch_all_data(url, output_file, params, date_key_api_min, date_key_api_max, date_key, desc=False, json=False):
    size = 10
    done = True

    # Make the initial request
    response = requests.get(url, params)
    # print("Response obtained.")
    if response.status_code not in [200, 206]:
        done = False
        print(f"Error: {response.status_code} - {response.text}")
        return 

    if json:
        data = response.json()
        df = pd.json_normalize(data['data'])
    else:
        content = response.content.decode('utf-8')
        df = pd.read_csv(StringIO(content), sep=";")

    df.to_csv(output_file, index=False, sep=";")

    # print("before while")
    while True:
        stop = len(df)
        if stop == 0 or stop < size:
            done = True
            break

        last_date = df[date_key].iloc[-1]
        last_date = pd.to_datetime(last_date)
        # print(last_date)

        if not desc:
            next_min_date = last_date + pd.Timedelta(days=1)
            params[date_key_api_min] = next_min_date.strftime('%Y-%m-%d')
        else:
            next_max_date = last_date - pd.Timedelta(days=1)
            params[date_key_api_max] = next_max_date.strftime('%Y-%m-%d')

        response = requests.get(url, params)
        if response.status_code not in [200, 206]:
            done = False
            print(f"Error: {response.status_code} - {response.text}")
            break

        if json:
            data = response.json()
            df = pd.json_normalize(data['data'])
        else:
            content = response.content.decode('utf-8')
            df = pd.read_csv(StringIO(content), sep=";")

        if len(df) == 0:
            done = True
            break

        df.to_csv(output_file, mode='a', index=False, header=False, sep=";")

    print("DONE", done)

params2 = {
    "size": 20000,
    "fields": "code_commune,nom_commune,date_prelevement,code_parametre,libelle_parametre,resultat_numerique,libelle_unite",
    "code_parametre": "1301,1302,1303,1295,1311,1312,1313,1314,1335,1340,1433,1382,1388,1387,1369,1383,1392,1449,1450",
    "code_departement": "75,77,78,91,92,93,94,95",
    "date_min_prelevement": "2014-01-01",
    "date_max_prelevement": "2024-01-01",
}

date_key_api_min2 = "date_min_prelevement"
date_key_api_max2 = "date_max_prelevement"
date_key2 = "date_prelevement"

url2 = "https://hubeau.eaufrance.fr/api/v1/qualite_eau_potable/resultats_dis"
output_file2 = "./data_API/analyses_eau_pot.csv"

fetch_all_data(
    url2,
    output_file2,
    params2,
    date_key_api_min2,
    date_key_api_max2,
    date_key2,
    desc=True,
    json=True
)
