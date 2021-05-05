
INSERT INTO Clients VALUES (1, "Jason", "Mathieu", "12 Rue des fleurs");
INSERT INTO Clients VALUES (2, "Grand", "Nicolas", "1 Avenue de la république");
INSERT INTO Clients VALUES (3, "Niel", "Jerome", "3 Rue des pommiers");
INSERT INTO Clients VALUES (4, "Buisson", "Camille", "5 Avenue de Gaulle");
INSERT INTO Clients VALUES (5, "James", "Laura", "18 Avenue des champs");
INSERT INTO Clients VALUES (6, "Fourrier", "Léa", "4 Rue de l'amande");


INSERT INTO Commandes VALUES (1,1,"Rue des fleurs", '2021-04-14', "transit");
INSERT INTO Commandes VALUES (2,1,"Rue de la liberté", '2021-04-15', "expediee");
INSERT INTO Commandes VALUES (3,2,"Rue des ecoles", '2021-04-11', "livree");
INSERT INTO Commandes VALUES (4,4, "Rue de la bastille", '2021-03-01', "transit");

INSERT INTO TypeArticles VALUES("NikeJordan", 199.99);
INSERT INTO TypeArticles VALUES("Skateboard", 19.83);
INSERT INTO TypeArticles VALUES("Lit", 500);
INSERT INTO TypeArticles VALUES("Manteau", 50.2);
INSERT INTO TypeArticles VALUES("iphone 10", 999);
INSERT INTO TypeArticles VALUES("macbook", 1999);
INSERT INTO TypeArticles VALUES("jouet", 10.83);
INSERT INTO TypeArticles VALUES("Tapis", 50.4);
INSERT INTO TypeArticles VALUES("peluche", 119.99);

INSERT INTO Entrepot VALUES("A", 83, "23 Rue des iles");
INSERT INTO Entrepot VALUES("A", 84, "23 Rue des iles");
INSERT INTO Entrepot VALUES("B", 10, "23 Rue des iles");
INSERT INTO Entrepot VALUES("A", 1, "23 Rue des iles");
INSERT INTO Entrepot VALUES("G", 24, "23 Rue des iles");
INSERT INTO Entrepot VALUES("G",1, "23 Rue des iles");
INSERT INTO Entrepot VALUES("G",2, "23 Rue des iles");
INSERT INTO Entrepot VALUES("G",3, "23 Rue des iles");
INSERT INTO Entrepot VALUES("G",4, "23 Rue des iles");
INSERT INTO Entrepot VALUES("G",5, "23 Rue des iles");


INSERT INTO Articles VALUES(11, "NikeJordan", "A", 84, "TRUE");
INSERT INTO Articles VALUES(12, "NikeJordan", "A", 83, "TRUE");
INSERT INTO Articles VALUES(13, "Skateboard", "B", 10, "TRUE");
INSERT INTO Articles VALUES(14, "Lit", "A", 1, "TRUE");
INSERT INTO Articles VALUES(15, "Manteau", "G", 24, "TRUE");
INSERT INTO Articles VALUES(16, "iphone 10", "G", 1, "TRUE");
INSERT INTO Articles VALUES(17, "macbook", "G", 2, "TRUE");
INSERT INTO Articles VALUES(18, "jouet", "G", 3, "TRUE");
INSERT INTO Articles VALUES(19, "Tapis", "G", 4, "TRUE");
INSERT INTO Articles VALUES(20, "peluche", "G", 5, "TRUE");

INSERT INTO Paniers VALUES (4,11);
INSERT INTO Paniers VALUES (1,12);
INSERT INTO Paniers VALUES (2,13);
INSERT INTO Paniers VALUES (3,14);
INSERT INTO Paniers VALUES (4,15);
