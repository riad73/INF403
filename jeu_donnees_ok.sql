INSERT INTO Clients VALUES (1, "Jason", "Kévin", "Rue des fleurs");
INSERT INTO Clients VALUES (2, "Gorur", "Selim", "Rue des glandeurs");
INSERT INTO Clients VALUES (3, "Guerbaa", "Rayan", "Rue du chomage");
INSERT INTO Clients VALUES (4, "Bouissa", "Ilyass", "Rue du dormeur");
INSERT INTO Clients VALUES (5, "Hadgverdi", "Nafiseh", "Rue de la gentilesse");
INSERT INTO Clients VALUES (6, "Fiori", "Victoria", "Rue du covid");


INSERT INTO Commandes VALUES (1,1,"Rue des fleurs", '2021-04-14', "transit");
INSERT INTO Commandes VALUES (2,1,"Rue des fleurs", '2021-04-15', "expédiée");
INSERT INTO Commandes VALUES (3,2,"Rue des ecoles", '2021-04-11', "livrée");
INSERT INTO Commandes VALUES (4,4, "Rue de la bastille", '2021-03-01', "transit");


INSERT INTO Paniers VALUES (1,12);
INSERT INTO Paniers VALUES (2,13);
INSERT INTO Paniers VALUES (3,14);
INSERT INTO Paniers VALUES (4,15);

INSERT INTO Articles VALUES(12, 1, "NikeJordan", "A", 83);
INSERT INTO Articles VALUES(13, 2, "Skateboard", "B", 10);
INSERT INTO Articles VALUES(14, 3, "Lit", "A", 1);
INSERT INTO Articles VALUES(15, 4, "Manteau", "G", 24);


INSERT INTO Entrepot VALUES("A", 83, 12);
INSERT INTO Entrepot VALUES("B", 10, 13);
INSERT INTO Entrepot VALUES("A", 1, 14);
INSERT INTO Entrepot VALUES("G", 24, 15);


INSERT INTO TypeArticles VALUES("NikeJordan", 12, 199.99);
INSERT INTO TypeArticles VALUES("Skateboard", 13, 19.83); 
INSERT INTO TypeArticles VALUES("Lit", 14, 500);
INSERT INTO TypeArticles VALUES("Manteau", 15, 50.2);
