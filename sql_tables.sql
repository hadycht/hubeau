CREATE DATABASE hubeau;
\connect hubeau;

CREATE TABLE communes_idf (
    code_commune VARCHAR(6) PRIMARY KEY,
    libelle_commune VARCHAR(255),
    code_departement VARCHAR(3),
    libelle_departement VARCHAR(255),
    code_bassin_DCE CHAR(1),
    libelle_bassin_DCE VARCHAR(255)
);

COPY communes_idf FROM '/home/hady/Bureau/M2/Data_Aqcuisition/Project/datasets/communes_IDF.csv' CSV header;

CREATE TABLE stations_pc_idf (
    code_station VARCHAR(10) PRIMARY KEY,
    libelle_station VARCHAR(255),
    code_commune VARCHAR(5) REFERENCES communes_idf,
    code_cours_eau VARCHAR(8),
    nom_cours_eau VARCHAR(255),
    date_creation DATE,
    date_arret DATE,
    date_maj_information DATE
);

COPY stations_pc_idf FROM '/home/hady/Bureau/M2/Data_Aqcuisition/Project/datasets/stations_pc_idf.csv' CSV header;

CREATE TABLE analyses_pc_idf (
    date_prelevement DATE,
    code_station VARCHAR(20) REFERENCES stations_pc_idf,
    code_parametre VARCHAR(5),
    libelle_parametre VARCHAR(255),
    resultat DECIMAL(10, 2),
    code_unite VARCHAR(5),
    symbole_unite VARCHAR(50),
    PRIMARY KEY (date_prelevement, code_station, code_parametre)
); 

COPY analyses_pc_idf FROM '/home/hady/Bureau/M2/Data_Aqcuisition/Project/datasets/analyses_pc.csv' CSV header; 

CREATE TABLE stations_piezo (
    code_bss VARCHAR(50) PRIMARY KEY,
    code_commune_insee VARCHAR(10) REFERENCES communes_idf
);

COPY stations_piezo FROM '/home/hady/Bureau/M2/Data_Aqcuisition/Project/datasets/stations_piezo.csv' DELIMITER ';' CSV header; 

CREATE TABLE piezometrie (
    code_bss VARCHAR(50) REFERENCES stations_piezo,
    date_mesure DATE,
    profondeur_nappe DECIMAL(10, 2),
    niveau_nappe_eau DECIMAL(10, 2),
    PRIMARY KEY (code_bss, date_mesure)
); 

COPY piezometrie FROM '/home/hady/Bureau/M2/Data_Aqcuisition/Project/datasets/piezometrie.csv' DELIMITER ';' CSV header; 

CREATE TABLE stations_qualite_nappes (
    bss_id VARCHAR(50) PRIMARY KEY,
    code_commune_insee VARCHAR(10) REFERENCES communes_idf
);

COPY stations_qualite_nappes FROM '/home/hady/Bureau/M2/Data_Aqcuisition/Project/datasets/stations_qualite_nappes.csv' DELIMITER ';' CSV header; 

CREATE TABLE analyses_qualite_nappes (
    bss_id VARCHAR(50) REFERENCES stations_qualite_nappes,
    date_debut_prelevement VARCHAR(5),
    code_param  VARCHAR(5),
    nom_param VARCHAR(255),
    resultat DECIMAL(10, 2),
    code_unite VARCHAR(5),
    nom_unite VARCHAR(50),
    PRIMARY KEY (bss_id, date_debut_prelevement, code_param)
);

COPY analyses_qualite_nappes FROM '/home/hady/Bureau/M2/Data_Aqcuisition/Project/datasets/resultat_qualite.csv' DELIMITER ';' CSV header; 


