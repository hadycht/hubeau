CREATE DATABASE hubeau;
\connect hubeau;

CREATE TABLE communes_idf (
    code_commune VARCHAR PRIMARY KEY,
    libelle_commune VARCHAR,
    code_departement VARCHAR,
    libelle_departement VARCHAR,
    code_bassin_DCE CHAR,
    libelle_bassin_DCE VARCHAR
);

COPY communes_idf FROM '/home/hady/Bureau/M2/Data_Aqcuisition/Project/data_cleaned/communes_IDF.csv' CSV header;

CREATE TABLE stations_pc_idf (
    code_station VARCHAR PRIMARY KEY,
    libelle_station VARCHAR,
    code_commune VARCHAR REFERENCES communes_idf,
    code_cours_eau VARCHAR,
    nom_cours_eau VARCHAR,
    date_creation DATE,
    date_arret DATE,
    date_maj_information DATE
);

COPY stations_pc_idf FROM '/home/hady/Bureau/M2/Data_Aqcuisition/Project/data_cleaned/stations_pc_idf.csv' CSV header;

CREATE TABLE analyses_pc_idf (
    date_prelevement DATE,
    code_station VARCHAR REFERENCES stations_pc_idf,
    code_parametre VARCHAR,
    libelle_parametre VARCHAR,
    resultat DECIMAL(10, 2),
    code_unite VARCHAR,
    symbole_unite VARCHAR,
    PRIMARY KEY (date_prelevement, code_station, code_parametre)
); 

COPY analyses_pc_idf FROM '/home/hady/Bureau/M2/Data_Aqcuisition/Project/data_cleaned/analyses_pc.csv' CSV header; 

CREATE TABLE stations_piezo (
    code_bss VARCHAR PRIMARY KEY,
    code_commune_insee VARCHAR REFERENCES communes_idf
);

COPY stations_piezo FROM '/home/hady/Bureau/M2/Data_Aqcuisition/Project/data_cleaned/stations_piezo.csv' DELIMITER ';' CSV header; 

CREATE TABLE piezometrie (
    code_bss VARCHAR REFERENCES stations_piezo,
    date_mesure DATE,
    profondeur_nappe DECIMAL(10, 2),
    niveau_nappe_eau DECIMAL(10, 2),
    PRIMARY KEY (code_bss, date_mesure)
); 

COPY piezometrie FROM '/home/hady/Bureau/M2/Data_Aqcuisition/Project/data_cleaned/piezometrie.csv' DELIMITER ';' CSV header; 

CREATE TABLE stations_qualite_nappes (
    bss_id VARCHAR PRIMARY KEY,
    code_commune_insee VARCHAR REFERENCES communes_idf
);

COPY stations_qualite_nappes FROM '/home/hady/Bureau/M2/Data_Aqcuisition/Project/data_cleaned/stations_qualite_nappes.csv' CSV header; 

CREATE TABLE analyses_qualite_nappes (
    bss_id VARCHAR REFERENCES stations_qualite_nappes,
    date_debut_prelevement VARCHAR,
    code_param  VARCHAR,
    nom_param VARCHAR,
    resultat DECIMAL(10, 2),
    code_unite VARCHAR,
    nom_unite VARCHAR,
    PRIMARY KEY (bss_id, date_debut_prelevement, code_param)
);

COPY analyses_qualite_nappes FROM '/home/hady/Bureau/M2/Data_Aqcuisition/Project/data_cleaned/resultat_qualite.csv' DELIMITER ';' CSV header; 

CREATE TABLE stations_ecoul_idf (
    code_station VARCHAR PRIMARY KEY,
    libelle_station VARCHAR, 
    code_commune VARCHAR REFERENCES communes_idf,
    code_departement VARCHAR,
    code_cours_eau VARCHAR,
    libelle_cours_eau VARCHAR,
    date_maj_station DATE
); 

COPY stations_ecoul_idf FROM '/home/hady/Bureau/M2/Data_Aqcuisition/Project/data_cleaned/stations_ecoul_idf.csv' CSV header; 

CREATE TABLE observations_ec (
    date_observation DATE,
    code_station VARCHAR REFERENCES stations_ecoul_idf,
    code_ecoulement VARCHAR,
    libelle_ecoulement VARCHAR,
    PRIMARY KEY(code_station, date_observation)
);

COPY observations_ec FROM '/home/hady/Bureau/M2/Data_Aqcuisition/Project/data_cleaned/analyses_ec.csv' CSV header; 

CREATE TABLE analyses_eau_potable (
    date_prelevement DATE,
    code_commune VARCHAR REFERENCES communes_idf,
    code_parametre VARCHAR,
    libelle_parametre VARCHAR,
    resultat_numerique DECIMAL(10, 2),
    libelle_unit VARCHAR,
    nom_commune VARCHAR,
    PRIMARY KEY (date_prelevement, code_commune, code_parametre)

); 

COPY analyses_eau_potable FROM '/home/hady/Bureau/M2/Data_Aqcuisition/Project/data_cleaned/analyses_eau_potable.csv' CSV header; 