mkdir data_API
mkdir data_cleaned

echo "Connecting to SANDRE API to get communes dataset"
echo "****** this may take a while *******"
bash communes_fr_sandre.bash 
sed '2d' ./data_API/communes_FR.csv > ./data_API/communes_fr.csv
echo "Cleaning the communes dataset"
python3 communes_fr_cleaning.py 
echo "DONE"

echo "Connecting to HubEAU API Qualité des cours d'eau: Endpoint Stations"
echo "****** this may take a while *******"
bash stations_pc_hubeau_api.bash 
echo "Cleaning Stations physico-chemical dataset"
python3 stations_pc_cleaning.py 
echo "DONE"

echo "Connecting to HubEAU API Qualité des cours d'eau: Endpoint analyses"
echo "****** this may take a while *******"
python3 analyses_pc_api.py 
echo "Cleaning analyses physico-chemical dataset"
python3 analyses_pc_cleaning.py 
rm ./temp.csv
echo "DONE"

echo "Connecting to HubEau API Ecoulement des cours d'eau: Endpoint Stations"
echo "****** this may take a while *******"
bash stations_ecoul_idf.bash 
echo "Cleaning Stations ecoulement dataset"
python3 stations_ecoul_cleaning.py 
echo "DONE"

echo "Connecting to HubEAU API Ecoulement des cours d'eau: Endpoint analyses, & cleaning"
echo "****** this may take a while *******"
python3 observations_ecoul.py 

echo "Connecting to HubEau API Qualité de l'eau potable: Endpoint analyses"
echo "****** this may take a while *******"
python3 analyses_eau_potable_api.py 
echo "Cleaning Analyses Eau potable dataset"
python3 analyses_eau_potable_cleaning.py 
echo "DONE"

echo "Connecting to HubEau API piézométrie: Endpoint Stations, & Cleaning" 
echo "****** this may take a while *******"
python3 stations_piezo.py 
echo "DONE"

echo "Connecting to Hubeau API piézométrie: Endpoint chroniques"
echo "****** this may take a while *******"
python3 piezometrie_api.py
echo "Cleaning Piezometrie Chroniques dataset"
python3 piezometrie_cleaning.py
echo "DONE"

echo "Connecting to HubEau API Qualité des nappes: Endpoint Stations, & Cleaning"
echo "****** this may take a while *******"
python3 stations_qualite_nappes.py 
echo "DONE"

echo "Connecting to Hubeau API Qualité des nappes: Endpoint analyses"
echo "****** this may take a while *******"
python3 qualite_nappe_api.py
echo "Cleaning Qualite Nappes Analyses dataset"
python3 qualite_nappe_cleaning.py
echo "DONE"

echo "ALL DATASETS ARE SAVED INTO THE FOLDER data_cleaned, YOU MAY USE IT NOW TO BUILD THE POSTGRESQL DATABASE USING THE FILE sql_tabes.sql"