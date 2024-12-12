# AquaInsight: Sandre & HubEau APIs 

In this project, we focused on assessing the water quality of rivers and water bodies in Île de France. We gathered different measurements since the 1st January 2014 until the last date the APIs provided. 

## API Sandre Communes de France 

This API provides data on the water bodies (same as HubEau, more or less). For more information, you can consult the [Sandre API Référentiel](https://www.sandre.eaufrance.fr/api-referentiel). 

We used this API to retrieve "Communes" in France that have water bodies in them. We used the *bash script* **communes_fr_sandre.bash** to get all the communes in France. 

Afterwards we used the *python script* **communes_fr_cleaning.py** to clean the retrieved dataset and focus on "Communes" of Île de France. 

## API HubEau: Qualité des cours d'eau 

This API provides data on the results of physico-chemical water quality measurements for rivers and water bodies submitted by the Water Agencies. For more information, you can consult the [API Quality of Watercourses documentation](https://hubeau.eaufrance.fr/page/api-qualite-cours-deau).

Thus, to retrieve the stations where the measurements were made, we use the *bach script* **stations_pc_hubeau_api.bash**. We afterwards clean the API dataset using the *python script* **stations_pc_cleaning.py**. 

To retrieve the different measurements, we use the *python script* **analyses_pc_api.py** (it was simpler to deal with pagination with python than bash). We afterwards cleaned this resulting dataset using the *python script* **analyses_pc_cleaning.py**. 

## API HubEau: Piezométrie

This API provides data on the depth and water level of underground aquifers. For more information, you can consult the [API Piezometrie documentation](https://hubeau.eaufrance.fr/page/api-piezometrie). 

Thus, to retrieve the stations where the measurements were made, we use the *python script* **stations_piezo.py**. 

To retrieve the different measurements, we use the *python script* **piezometrie_api.py**  We afterwards cleaned this resulting dataset using the *python script* **piezometrie_cleaning.py**. 

## API HubEau: Qualité des nappes d'eau souterraine

This API provides data on the results of physico-chemical water quality measurements for underground aquifers. For more information, you can consult the [API Quality of underground aquifers documentation](https://hubeau.eaufrance.fr/page/api-qualite-nappes).

Thus, to retrieve the stations where the measurements were made, we use the *python script* **stations_qualite_nappes.py**.

To retrieve the different measurements, we use the *python script* **qualite_nappe_api.py**. We afterwards cleaned this resulting dataset using the *python script* **stations_qualite_nappes.py**. 