INSERT INTO Clients VALUES (1, "Jason", "Mathieu", "12 Rue des fleurs");
INSERT INTO Clients VALUES (2, "Grand", "Nicolas", "1 Avenue de la république");
INSERT INTO Clients VALUES (3, "Niel", "Jerome", "3 Rue des pommiers");
INSERT INTO Clients VALUES (4, "Buisson", "Camille", "5 Avenue de Gaulle");
INSERT INTO Clients VALUES (5, "James", "Laura", "18 Avenue des champs");
INSERT INTO Clients VALUES (6, "Fourrier", "Léa", "4 Rue de l'amande");


INSERT INTO Commandes VALUES (1,1,"12 Rue des fleurs", '2021-04-14', "transit");
INSERT INTO Commandes VALUES (2,1,"1 Avenue de la république", '2021-04-15', "expédiée");
INSERT INTO Commandes VALUES (3,2,"Rue des ecoles", '2021-04-11', "livrée");
INSERT INTO Commandes VALUES (4,4, "5 Avenue de Gaulle", '2021-03-01', "transit");


INSERT INTO Paniers VALUES (1,12);
INSERT INTO Paniers VALUES (2,13);
INSERT INTO Paniers VALUES (3,14);
INSERT INTO Paniers VALUES (4,15);

INSERT INTO Entrepot VALUES("A", 83, 12);
INSERT INTO Entrepot VALUES("B", 10, 13);
INSERT INTO Entrepot VALUES("A", 1, 14);
INSERT INTO Entrepot VALUES("G", 24, 15);
INSERT INTO Entrepot VALUES("G",1, 16);

INSERT INTO TypeArticles VALUES("NikeJordan", 12, 199.99);
INSERT INTO TypeArticles VALUES("Skateboard", 13, 19.83); 
INSERT INTO TypeArticles VALUES("Lit", 14, 500);
INSERT INTO TypeArticles VALUES("Manteau", 15, 50.2);
INSERT INTO TypeArticles VALUES("iphone 10", 16, 9.99);

INSERT INTO Articles VALUES(12, "NikeJordan", "A", 83);
INSERT INTO Articles VALUES(13, "Skateboard", "B", 10);
INSERT INTO Articles VALUES(14, "Lit", "A", 1);
INSERT INTO Articles VALUES(15, "Manteau", "G", 24);
INSERT INTO Articles VALUES(16, "iphone 10", "G", 1);




