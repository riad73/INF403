# Création d'une marketplace
## Le but de ce projet est de pouvoir créer une base de donnée relationnelle.


**Objectif:**
  - Partie I : Description du problème & modèle conceptuel.
  - Partie II : Traduction du modèle UML au relationnel.
  - Partie III : Mettre en œuvre quelques fonctionnalitées simplifiées d’une application Python & SQLite

**To do:**

  - [x] Partie 1
  - [ ] Partie 2(en cours)
  - [ ] Partie 3

### Partie 1: Description du problème & modèle conceptuel.

Dans ce projet, nous souhaitons créer la base de donnée d'un marketplace pour notre client.
Le principe d'une marketplace et de pouvoir mettre en relation client et vendeur sur une même application. 
Voici les notions que le client souhaite que l'on mette en oeuvre:


**Les clients :** Les clients sont identifiés par un numéro unique, on représente aussi leur nom, prénom et date de naissance.


**Les fournisseurs :** Les fournisseurs sont identifiés par un numéro et une marque ils mettent en avant sur l'application un ou plusieur articles de cette même marque. Les articles présent sur le site sont mis par le fournisseur en quantité limité et seront stocké dans l'entrepot de la société de la marketplace. Dans l'entrepot le stock d'article se situe dans une allée qui est identifiable par une caractère et stocké à un numéro dans cette même allée.


**Les commandes**: Le dirigeant de la marketplace veut par la même occasion qu'une fois que le client séléctionne un seul et unique article, il passe commande tout de suite après. La commande sera donc identifié par un numéro de commande et comportera, le nom du client, son adresse, la référence de l'article en question, la date d'achat ainsi que le statut de la commande (expédié, en transit ou livré).


*Conception de notre diagramme UML*
Grâce à ces information nous pouvons traduire les demandes du client en faisant notre conception du diagramme UML.

![image](https://user-images.githubusercontent.com/58702474/113482416-f4ef5000-949e-11eb-8df0-a290c7b0bb56.png)

### Partie 2: Traduction du modèle UML au relationnel.

A partir du diagramme UML nous allons déduire ci-dessous le modèle relationnel.


**Clients**(numero_client


