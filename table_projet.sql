DROP TABLE IF EXISTS Clients;
DROP TABLE IF EXISTS Commandes;
DROP TABLE IF EXISTS Articles;
DROP TABLE IF EXISTS TypeArticles;
DROP TABLE IF EXISTS Entrepot;

PRAGMA FOREIGN_KEYS=ON;

CREATE TABLE Clients(
	numero_client INTEGER NOT NULL,
	nom TEXT, 
	prenom TEXT ,
	adresse TEXT NOT NULL,
	CONSTRAINT cl_pk PRIMARY KEY (numero_client)
);
	
	
CREATE TABLE Paniers(
	numero_commande INTEGER NOT NULL,
	numero_client INTEGER NOT NULL
);

CREATE TABLE Commandes(
	numero_commande INTEGER NOT NULL,
	numero_client INTEGER NOT NULL,
	adresse_livraison TEXT NOT NULL,
	date_achat DATE NOT NULL,
	statut TEXT NOT NULL,
	CONSTRAINT com_pk PRIMARY KEY (numero_commande),
	CONSTRAINT com_ck CHECK (statut in ("expediée", "transit", "livrée"))
);
	
CREATE TABLE Articles(
	reference_article INTEGER NOT NULL,
	CONSTRAINT art_pk PRIMARY KEY (reference_article)
);

CREATE TABLE TypeArticles(
	nom_article TEXT NOT NULL,
	reference_article INTEGER NOT NULL,
	prix FLOAT NOT NULL,
	stock INTEGER NOT NULL,
	CONSTRAINT typ_art_pk PRIMARY KEY (nom_article)
);

CREATE TABLE Entrepot(
	reference_article INTEGER NOT NULL,
	allee CHAR NOT NULL,
	position INTEGER NOT NULL,
	CONSTRAINT ent_pk PRIMARY KEY (allee, position)
);
	
	
