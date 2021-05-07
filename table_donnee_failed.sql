-- Voici les tests échoués.

--Inserer un client avec un numéro client déjà utilisé.
INSERT INTO Clients VALUES (1, "Gaillard", "Alix", "Rue des pommes");

--Inserer un client avec un numéro client qui est négatif.
INSERT INTO Clients VALUES (-1, "Gaillard", "Alix", "Rue des pommes");

--Inserer une commande dans un numéro de commande déjà attribué.
INSERT INTO Commandes VALUES (1,1,"Rue de la poire", '2021-03-11', "transit");

--Inserer une commande avec un statut inconnu
INSERT INTO Commandes VALUES (10,1,"Rue de la pomme", '2021-03-11', "en avion");

--Inserer dans un panier deux fois une meme référence d'article
INSERT INTO Paniers VALUES (4,12);

--Inserer dans le panier une reference d'article qui n'existe pas
INSERT INTO Paniers VALUES (4,1000);

--Inserer dans l'entrepot un article sur une place déjà attribué.
INSERT INTO Entrepot VALUES("A", 83, "21 rue de la libération");

--Inserer dans l'entrepot un article sur une place avec un nombre négatif.
INSERT INTO Entrepot VALUES("A", -8, "21 rue de la libération");

--Inserer dans l'entrepot le meme article
INSERT INTO Entrepot VALUES("G",1, "21 rue de la libération");

--Inserer un article déjà inseré
INSERT INTO Articles VALUES(12, "NikeJordan", "A", 83, "TRUE");

--Inserer un article avec un mauvais termes dans l'attibut disponible
INSERT INTO Articles VALUES(12, "NikeJordan", "A", 83, "VRAI");

--Inserer un article qui n'est pas présent dans type article ni dans l'entrepot
INSERT INTO Articles VALUES(17, "Nitendo Switch", "A", 16);

--Inserer un article qui est présent dans type article mais pas dans l'entrepot
INSERT INTO Articles VALUES(17, "Caméra S3", "D", 2);

--Inserer un prix negatif ou egale à 0
INSERT INTO TypeArticles VALUES ("Tablette", -200.3);


