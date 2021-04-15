-- Ceci sont les tests échoués.

--Inserer un client avec un numéro client déjà utilisé.
INSERT INTO Clients VALUES (1, "Gaillard", "Alix", "Rue des pommes");

--Inserer une commande dans un numéro de commande déjà attribué.
INSERT INTO Commandes VALUES (1,1,"Rue de la poire", '2021-03-11', "transit");

--Inserer dans un panier deux fois une meme référence d'article
INSERT INTO Paniers VALUES (4,12);

--Inserer dans l'entrepot un article sur une place déjà attribué.
INSERT INTO Entrepot VALUES("A", 83, 16);

--Inserer dans l'entrepot un article dans une allée nommé par une chaine de caractère
INSERT INTO Entrepot VALUES("A", 83, 16);
