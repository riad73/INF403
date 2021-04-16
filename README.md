# Création d'une boutique en ligne
## Le but de ce projet est de pouvoir créer une base de donnée relationnelle.


**Objectif:**
  - Partie I : Description du problème & modèle conceptuel.
  - Partie II : Traduction du modèle UML au relationnel.
  - Partie III : Mettre en œuvre quelques fonctionnalitées simplifiées d’une application Python & SQLite

**To do:**

  - [x] Partie I
  - [x] Partie II 
  - [ ] Partie III

### Partie 1: Description du problème & modèle conceptuel.

Dans ce projet, nous souhaitons créer la base de donnée d'une boutique en ligne pour un client.
Le principe d'une boutique en ligne est de pouvoir mettre en relation clients et articles sur une même application.
Voici les notions que le client souhaite que l'on mette en oeuvre:


**Les clients :** Les clients sont identifiés par un numéro unique, on représente aussi leur nom, prénom, adresse et date de naissance.

**Les articles :** Les articles seront identifiable par un numéro qui correspond à la référence de l'article. De plus, les articles présent sur l'application auront un nom, une marque ainsi qu'un prix. Ces articles seront stockés dans l'entrepot de la boutique en ligne. Cet entrepot possède des allées correspondant à un caractère du type : "A", "B"... et sont positionnés à un endroit étiquetté par un numéro.

**Les commandes**: Les commandes quant à elle sont identifiable par un numéro de commande et comportera, le nom du client, son adresse de livraison, la référence de l'article commandé, la date d'achat ainsi que le statut de la commande (expédié, en transit ou livré). De plus, toutes les commandes effectuées seront stockées dans le panier de mes clients.


*Conception de notre diagramme UML* <br/>
Grâce aux informations ci-dessus nous pouvons traduire les demandes du client par un diagramme UML.

![image](https://user-images.githubusercontent.com/58702474/115018483-34169b80-9eb8-11eb-9317-6ce99ddb11a5.png)

### Partie 2: Traduction du modèle UML au relationnel. <br/>
<br/>

A partir du diagramme UML nous allons déduire ci-dessous le modèle relationnel.<br/>

Pour designer une clé primaire nous utiliserons une typographie bold et italique, _exemple_ **_userID_** <br/>

**Clients**(**_numero_client_**, nom, prenom, adresse) <br/>
/* <i, n, p, a> ∈ Clients ⇐⇒ le client est indentifié par un numéro i, un prénom p, un nom m et une adresse a */<br/>


**Commandes**(**_numero_commande_**, numero_client, adresse_livraison, date_achat, statut) <br/>
/* <k, i, l, d, s> ∈ Commandes ⇐⇒ la commande est identifié par un numéro de commande k, un numéro client qui a effectué une commande i, une adresse de livraison l, une date d'achat d et un statut de l'avancement de la commande s */<br/>


**Paniers**(**_reference_article_**, numero_commande) <br/>
/* <r, k> ∈ Paniers ⇐⇒ le panier contient le numéro de la commande k et la référence de l'article r */<br/>

**Articles**(**_reference_article_**, nom_article, allée, place) <br/>
/* <r, na, m, o> ∈ Articles ⇐⇒ l'article est indentifié par une référence r, un nom na, une allée m ainsi qu'une place dans l'allée o*/<br/>
  
**TypeArticles**(**_nom_article_**, reference_article, prix) <br/>
/* <a, r, p> ∈ TypeArticles ⇐⇒ le type d'article est identifié par une nom d'article a, une référence r et un prix p*/<br/>
  
**Entrepot**(**_allée, position_**, référence_article) <br/>
  /* <m, o, r> ∈ Entrepot ⇐⇒ les articles sont stockés par une référence d'article r dans un entrepot et est indentifiable par une allée m et une position o*/<br/>
<br/>
<br/>

Les domaines sont:<br/>
domaine(numero_client)=domaine(numero_commande)=domaine(place)=domaine(reference_article)=domaine(prix) = entier > 0 <br/>
domaine(nom)=domaine(prenom)=domaine(adresse)=domaine(adresse_livraison)=domaine(statut)=domaine(nom_article) = domaine(allee) = chaine de caractère <br/>
domaine(date_achat) = date <br/>
<br/>
<br/>
<br/>
Commandes[numero_client] ⊆ Client [numero_client] <br/>

Paniers[numero_commande] ⊆ Commandes[numero_commande] <br/>

Paniers[reference_article] ⊆ Articles[reference_article] <br/>

Articles[allee, position] ⊆ Entrepot[allee, position]<br/>

Articles[nom_article] ⊆ TypeArticles[nom_article]<br/>

StatutCommande ∈ {expidée, transit, livrée}
