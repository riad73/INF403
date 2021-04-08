# Création d'une boutique en ligne
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

Dans ce projet, nous souhaitons créer la base de donnée d'une boutique en ligne pour un client.
Le principe d'une boutique en ligne est de pouvoir mettre en relation clients et articles sur une même application.
Voici les notions que le client souhaite que l'on mette en oeuvre:


**Les clients :** Les clients sont identifiés par un numéro unique, on représente aussi leur nom, prénom, adresse et date de naissance.

**Les articles :** Les articles seront identifiable par un numéro qui correspond à la référence de cet article. Deplus, on affichera le nom de l'article, sa marque, le fournisseur, son prix et sa quantité (stock). Ces articles seront stockés dans l'entrepot de la boutique la boutique en ligne. Ils sont rangés dans une allée correspondant à un caractère type : "A", "B"... et seront positionnés à un endroit étiquetté par un numéro.

**Les commandes**: Les commandes quant à elle sont identifiable par un numéro de commande et comportera, le nom du client, son adresse, la référence de l'article en question, la date d'achat ainsi que le statut de la commande (expédié, en transit ou livré). Toutes les commandes seront alors stockés dans le panier de mes clients.


*Conception de notre diagramme UML* <br/>
Grâce aux informations ci-dessus nous pouvons traduire les demandes du client par un diagramme UML.

![image](https://user-images.githubusercontent.com/58702474/114061642-f356cb00-9896-11eb-99b6-e6515019c94b.png)





### Partie 2: Traduction du modèle UML au relationnel.

A partir du diagramme UML nous allons déduire ci-dessous le modèle relationnel.<br/>

Pour designer une clé primaire nous utiliserons une typographie bold et italique, _exemple_ **_userID_** <br/>

**Clients**(**_numero_client_**, nom, prenom, adresse) <br/>

**Paniers**(numero_client, reference_article) <br/>

**Commandes**(**_numero_commande_**, numero_client, adresse_livraison, date_achat, statut) <br/>

**Articles**(**_reference_article_**, nom_article) <br/>

**TypeArticles**(**_reference_article_**, prix, stock) <br/>

**Entrepot**(**_reference_article_**, allée, place) <br/>



Clients(numero_client) ⊆  Commandes(numero_client) <br/>

Commandes(reference_article) ⊆  Articles(reference_article) <br/>

Articles(reference_article) ⊆  Commandes(reference_article) <br/>

Articles(reference_article) = TypeArticles(reference_article) <br/>

Articles(reference_article) ⊆  Entrepot(reference_article) <br/>

