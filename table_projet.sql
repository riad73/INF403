DROP TABLE IF EXISTS TypeArticles;
DROP TABLE IF EXISTS Paniers;
DROP TABLE IF EXISTS Articles;
DROP TABLE IF EXISTS Entrepot;
DROP TABLE IF EXISTS Commandes;
DROP TABLE IF EXISTS Clients;



PRAGMA FOREIGN_KEYS=ON;

CREATE TABLE Clients(
	numero_client INTEGER NOT NULL,
	nom TEXT, 
	prenom TEXT ,
	adresse TEXT NOT NULL,
	CONSTRAINT cl_pk PRIMARY KEY (numero_client),
	CONSTRAINT cl_ck CHECK ((numero_client) > 0)
);
	
	

CREATE TABLE Commandes(
	numero_commande INTEGER NOT NULL,
	numero_client INTEGER NOT NULL,
	adresse_livraison TEXT NOT NULL,
	date_achat DATE NOT NULL,
	statut TEXT NOT NULL,
	CONSTRAINT com_pk PRIMARY KEY (numero_commande),
	CONSTRAINT com_fk FOREIGN KEY (numero_client) REFERENCES Clients(numero_client),
	CONSTRAINT com_ck1 CHECK (statut in ("expédiée", "transit", "livrée")),
	CONSTRAINT com_ck2 CHECK ((numero_commande) > 0)
	
);

CREATE TABLE Paniers(
	numero_commande INTEGER NOT NULL,
	reference_article INTEGER NOT NULL,
	CONSTRAINT pa_ck PRIMARY KEY (reference_article),
	CONSTRAINT pa_fk1 FOREIGN KEY (numero_commande) REFERENCES Commandes(numero_commande),
	CONSTRAINT pa_fk2 FOREIGN KEY (reference_article) REFERENCES Articles(reference_article)
);

CREATE TABLE Entrepot(
	allee CHAR NOT NULL,
	place INTEGER NOT NULL,
	reference_article INTEGER NOT NULL,
	CONSTRAINT ent_pk PRIMARY KEY (allee, position),
	CONSTRAINT ent_ck CHECK ((place) > 0)
	
);
CREATE TABLE Articles(
	reference_article INTEGER NOT NULL,
	nom_article TEXT NOT NULL,
	allee CHAR NOT NULL,
	place INTEGER NOT NULL,
	CONSTRAINT art_pk PRIMARY KEY (reference_article),
	CONSTRAINT art_fk1 FOREIGN KEY (allee,place) REFERENCES Entrepot(allee,place),
	CONSTRAINT art_fk2 FOREIGN KEY (nom_article) REFERENCES TypeArticles(nom_article),
	CONSTRAINT art_ck CHECK ((place) > 0)
);

CREATE TABLE TypeArticles(
	nom_article TEXT NOT NULL,
	prix FLOAT NOT NULL,
	CONSTRAINT typ_art_pk PRIMARY KEY (nom_article),
	CONSTRAINT typ_art_ck CHECK ((prix) >0)
);

