DROP TABLE IF EXISTS Clients;
DROP TABLE IF EXISTS Paniers;
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
	reference_article INTEGER NOT NULL,
	CONSTRAINT pa_ck PRIMARY KEY (reference_article),
	CONSTRAINT pa_fk FOREIGN KEY (numero_commande) references Commandes(numero_commande)
);

CREATE TABLE Commandes(
	numero_commande INTEGER NOT NULL,
	numero_client INTEGER NOT NULL,
	adresse_livraison TEXT NOT NULL,
	date_achat DATE NOT NULL,
	statut TEXT NOT NULL,
	CONSTRAINT com_pk PRIMARY KEY (numero_commande),
	CONSTRAINT com_fk FOREIGN KEY (numero_client) references Clients(numero_client),
	CONSTRAINT com_ck CHECK (statut in ("expediée", "transit", "livrée"))
	
);
	
CREATE TABLE Articles(
	reference_article INTEGER NOT NULL,
	numero_commande INTEGER NOT NULL,
	nom_article TEXT NOT NULL,
	allée INTEGER NOT NULL,
	position INTEGER NOT NULL,
	CONSTRAINT art_pk PRIMARY KEY (reference_article),
	CONSTRAINT art_fk1 FOREIGN KEY (reference_article) references Paniers(reference_article),
	CONSTRAINT art_fk2 FOREIGN KEY (numero_commande) references Commandes(numero_commande)
);

CREATE TABLE TypeArticles(
	nom_article TEXT NOT NULL,
	reference_article INTEGER NOT NULL,
	prix FLOAT NOT NULL,
	CONSTRAINT typ_art_pk PRIMARY KEY (nom_article),
	CONSTRAINT typ_art_fk1 FOREIGN KEY (nom_article) references Articles(nom_article)
);

CREATE TABLE Entrepot(
	allee CHAR NOT NULL,
	position INTEGER NOT NULL,
	reference_article INTEGER NOT NULL,
	CONSTRAINT ent_pk PRIMARY KEY (allee, position),
	CONSTRAINT ent_fk FOREIGN KEY (allee, position) references Articles(allee, position)
);
	
	
