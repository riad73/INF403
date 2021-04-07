# Création d'une marketplace
## Le but de ce projet est de pouvoir créer une base de donnée relationnelle.


**Objectif:**
  - Partie I : Description du problème & modèle conceptuel.
  - Partie II : Traduction du modèle UML au relationnel.
  - Partie III : Mettre en œuvre quelques fonctionnalitées simplifiées d’une application Python & SQLite

**To do:**

  - [x] Partie I
  - [ ] Partie II (en cours)
  - [ ] Partie III

### Partie 1: Description du problème & modèle conceptuel.

Dans ce projet, nous souhaitons créer la base de donnée d'une marketplace pour notre client.
Le principe d'une marketplace et de pouvoir mettre en relation client et vendeur (fournisseur) sur une même application. 
Voici les notions que le client souhaite que l'on mette en oeuvre:


**Les clients :** Les clients sont identifiés par un numéro unique, on représente aussi leur nom, prénom, adresse et date de naissance.


**Les vendeurs :** Les vendeurs sont identifiés par un numéro et une marque. Ils metteront en avant sur l'application un ou plusieur articles de cette même marque. Les articles présent sur le site sont mis par le vendeurs en quantité limité et seront stockés dans l'entrepot de la société de la marketplace. Dans l'entrepot le stock d'articles se situent dans une allée qui est identifiable par un caractère ("A", "B"...)  et sont stockés à un numéro (qui réprésente la position) dans cette même allée.

**Les articles :** Les articles seront identifiable par un numéro qui correspond à la référence de cet article. Deplus, on affichera le nom de l'article, sa marque, le fournisseur, son prix et sa quantité (stock).

**Les commandes**: Les commandes sont donc identifiable par un numéro de commande et comportera, le nom du client, son adresse, la référence de l'article en question, la date d'achat ainsi que le statut de la commande (expédié, en transit ou livré).


*Conception de notre diagramme UML* <br/>
Grâce aux informations ci-dessus nous pouvons traduire les demandes du client par un diagramme UML.

![image](https://user-images.githubusercontent.com/58702474/113861067-13a75c80-97a7-11eb-839a-dbb5a92922c1.png)



### Partie 2: Traduction du modèle UML au relationnel.

A partir du diagramme UML nous allons déduire ci-dessous le modèle relationnel.<br/>

Pour designer une clé primaire nous utiliserons une typographie bold et italique, _exemple_ **_userID_** <br/>

**Clients**(**_numero_client_**, nom, prenom, adresse) <br/>

**Commandes**(**_numero_commande_**, num_client, reference_article, adresse_livraison, date_achat, statut) <br/>

**Articles**(**_reference_article_**, nom_article, numero_fournisseur, prix, nombre_articles) <br/>

**Vendeurs**(**_numero_fournisseur_**, marque) <br/>

**Entrepot**(**_reference_article_**, allée, numero_place) <br/>



Clients(numero_client) ⊆  Commandes(numero_client) <br/>

Articles(reference_article) ⊆  Commandes(reference_article) <br/>

Articles(reference_article) = Entrepot(reference_article) <br/>

Vendeur(numero_fournisseur) =  Articles(numero_fournisseur) <br/>

