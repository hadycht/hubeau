import requests

url = "https://hubeau.eaufrance.fr/api/v2/qualite_rivieres/station_pc.csv"
output_file = 'data_API/stations_pc.csv'

regions = {
    "84": "Auvergne-Rhône-Alpes",
    "27": "Bourgogne-Franche-Comté",
    "53": "Bretagne",
    "24": "Centre-Val de Loire",
    "94": "Corse",
    "44": "Grand Est",
    "32": "Hauts-de-France",
    "11": "Île-de-France",
    "28": "Normandie",
    "75": "Nouvelle-Aquitaine",
    "76": "Occitanie",
    "52": "Pays de la Loire",
    "93": "Provence-Alpes-Côte d'Azur",
    "01": "Guadeloupe",
    "02": "Martinique",
    "03": "Guyane",
    "04": "La Réunion",
    "06": "Mayotte"
} 

mode = 'wb'
for code_region, region_name in regions.items():
    print(f"Fetching data for region {region_name} (Code: {code_region})")

    # Inclure le code_region comme paramètre dans la requête API
    params = {
        'size': 20000,
        'code_region': code_region
    }

    response = requests.get(url, params)

    if response.status_code not in [200, 206] : 
        print('Error while connecting to the HubEau Qualite des eaux API, endpoint station_pc')

    with open(output_file, mode) as f : 
        f.write(response.content)

    mode = 'ab'
    # while True : 
    #     if "next" not in response.links : 
    #         break 
        
    #     next_url = response.links['next']['url']
    #     print(next_url)
    #     response = requests.get(next_url)
    #     print(response.content)
    #     if response.status_code not in [200, 206] : 
    #         print(response.status_code)
    #         print('Error while connecting to the HubEau Qualite des eaux API, endpoint station_pc')

    #     with open(output_file, 'ab') as f : 
    #         f.write(response.content)
        
    print("DONE")