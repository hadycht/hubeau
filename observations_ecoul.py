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

# First API call parameters
params1 = {
    "size": 20000,
    "code_departement": "75,77,78,91,92,93,94,95",
    "fields": (
        "code_station,code_ecoulement,libelle_ecoulement,date_observation"
    ),
    "date_observation_min": "2014-01-01",
    "date_observation_max": "2024-12-01"
}

date_key_api_min1 = "date_observation_min"
date_key_api_max1 = "date_observation_max"
date_key1 = "date_observation"

url1 = "https://hubeau.eaufrance.fr/api/v1/ecoulement/observations"
output_file1 = "./data_API/analyses_ec.csv"

fetch_all_data(
    url1,
    output_file1,
    params1,
    date_key_api_min1,
    date_key_api_max1,
    date_key1,
    desc=False,
    json=True
)

df_analyses = pd.read_csv('./data_API/analyses_ec.csv', sep=';')

# print(df_analyses.info())

df_analyses = df_analyses.dropna(subset=['code_ecoulement'])
# print(df_analyses.info())

df_stations = pd.read_csv('./data_cleaned/stations_ecoul_idf.csv')
df_analyses = df_analyses[df_analyses['code_station'].isin(df_stations['code_station'])] 

result = df_analyses.groupby(['date_observation','code_station'], as_index=False).agg({
    'code_ecoulement' : 'first',
    'libelle_ecoulement' : 'first'
})

result.to_csv('data_cleaned/analyses_ec.csv', sep=',', index=False)