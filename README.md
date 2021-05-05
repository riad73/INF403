# Création d'une boutique en ligne
## Le but de ce projet est de pouvoir créer une base de donnée relationnelle.


**Objectif:**
  - Partie I : Description du problème & modèle conceptuel.
  - Partie II : Traduction du modèle UML au relationnel.
  - Partie III : Mettre en œuvre quelques fonctionnalitées simplifiées d’une application Python & SQLite

**To do:**

  - [x] Partie I
  - [x] Partie II 
  - [x] Partie III

### Partie 1: Description du problème & modèle conceptuel.

Dans ce projet, nous souhaitons créer la base de donnée d'une boutique en ligne pour un client.
Le principe d'une boutique en ligne est de pouvoir mettre en relation clients et articles sur une même application.
Voici les notions que le client souhaite que l'on mette en oeuvre:


**Les clients :** Les clients sont identifiés par un numéro unique, on représente aussi leur nom, prénom, adresse et date de naissance.

**Les articles :** Les articles seront identifiable par un numéro qui correspond à la référence de l'article. De plus, les articles présent sur l'application auront un nom, une marque ainsi qu'un prix. Ces articles seront stockés dans l'entrepot de la boutique en ligne. Cet entrepot possède des allées correspondant à un caractère du type : "A", "B"... et sont positionnés à des endroits étiquettés par un numéro. Pour faciliter la gestion des articles les vendeurs souhaitent pouvoir gerer le stock, de même il souhaite pouvoir indiquer si un articile est disponible ou non.

**Les commandes**: Les commandes quant à elle sont identifiable par un numéro de commande et comportera, le nom du client, son adresse de livraison, la référence de l'article commandé, la date d'achat ainsi que le statut de la commande (expédié, en transit ou livré). De plus, toutes les commandes effectuées seront stockées dans le panier des clients.


*Conception de notre diagramme UML* <br/>
Grâce aux informations ci-dessus nous pouvons traduire les demandes du client par un diagramme UML.

![image](https://user-images.githubusercontent.com/58702474/116275552-09fc8d80-a784-11eb-962e-65995bb4d9b0.png)


### Partie 2: Traduction du modèle UML au relationnel. <br/>
<br/>


**Règles de traductions:**</br>
Nom classe singulier → Nom table pluriel </br>
CamelCase → Snake_case </br>
attribut → attribut_nomclasse </br>
/attribut  → view </br>
</br>
A partir du diagramme UML nous allons déduire ci-dessous le modèle relationnel.<br/>

Pour designer une clé primaire nous utiliserons une typographie bold et italique, _exemple_ **_userID_** <br/>

**Clients**(**_numero_client_**, nom, prenom, adresse) <br/>
/* <i, n, p, a> ∈ Clients ⇐⇒ le client est indentifié par un numéro i, un prénom p, un nom m et une adresse a */<br/>


**Commandes_base**(**_numero_commande_**, numero_client, adresse_livraison, date_achat, statut) <br/>
/* <k, i, l, d, s> ∈ Commandes ⇐⇒ la commande est identifié par un numéro de commande k, un numéro client qui a effectué une commande i, une adresse de livraison l, une date d'achat d et un statut de l'avancement de la commande s */<br/>

**(View) Commandes_base**(**_numero_commande_**, numero_client, adresse_livraison, date_achat, statut, quantite) <br/>
/* <k, i, l, d, s, q> ∈ Commandes ⇐⇒ la commande est identifié par un numéro de commande k, un numéro client qui a effectué une commande i, une adresse de livraison l, une date d'achat d, un statut de l'avancement de la commande s et le nombre d'articles dans la commmande q*/<br/>

**Paniers**(**_reference_article_**, numero_commande) <br/>
/* <r, k> ∈ Paniers ⇐⇒ le panier contient le numéro de la commande k et la référence de l'article r */<br/>

**Articles**(**_reference_article_**, nom_article, allée, place, disponible) <br/>
/* <r, na, m, o, di> ∈ Articles ⇐⇒ l'article est indentifié par une référence r, un nom na, une allée m ainsi qu'une place dans l'allée o. De plus la diponibilité de l'article est définie par une booléen di*/<br/>
  
**TypeArticles_base**(**_nom_article_**, prix) <br/>
/* <a, p> ∈ TypeArticles ⇐⇒ le type d'article est identifié par une nom d'article a et un prix p */<br/>

**(View) TypeArticles**(**_nom_article_**, prix, stock) <br/>
/* <a, p, st> ∈ TypeArticles ⇐⇒ le type d'article est identifié par une nom d'article a , un prix p et un stock st*/<br/>
  
**Entrepot**(**_allée, position_**, adresse_entrepot) <br/>
  /* <m, o, ad> ∈ Entrepot ⇐⇒ les articles sont stockés dans un entrepot et sont indentifiable par une allée m, une position o et une adresse ad */<br/>
<br/>
<br/>

Les domaines sont:<br/>
domaine(numero_client)=domaine(numero_commande)=domaine(place)=domaine(reference_article)=domaine(prix)=domaine(stock)=domaine(quantite) = entier > 0 <br/>
domaine(nom)=domaine(prenom)=domaine(adresse)=domaine(adresse_livraison)=domaine(statut)=domaine(nom_article) = domaine(allee) = domaine(adresse_entrepot)=domaine(disponible) = chaine de caractère <br/>
domaine(date_achat) = date <br/>
<br/>
<br/>
<br/>


Commandes[numero_client] ⊆ Client [numero_client] <br/>

Paniers[numero_commande] = Commandes[numero_commande] <br/>

Paniers[reference_article] ⊆ Articles[reference_article] <br/>

Articles[allee, place] = Entrepot[allee, place]<br/>

Articles[nom_article] = TypeArticles[nom_article]<br/>

StatutCommande ∈ {expidée, transit, livrée} <br/>

Disponible ∈ {TRUE, FALSE} <br/>

<br/>
<br/>

### Partie 3: Réalisation d'une application Python. <br/>

#### Connexion </br>
A partir du menu d'authentification (après l'éxecution de la commande [c] se connecter) vous avez le choix de vous connecter sur différents comptes: <br/>
![image](https://user-images.githubusercontent.com/58702474/117122099-cadac780-ad95-11eb-8a2f-b246761dd9e5.png)

- Identification classique<br/>
                       ``` numero du compte```
      L'identification classique permet à l'utilisateur d'avoir l'expérience d'un client dans une boutique ordinaire. Il peut donc par le menu naviguer sur différentes sections tel que la visualisation de ses dernieres commandes, le catalogue ou encore l'achat. <br/>
      _exemple: Entrez votre numéro de compte: 1_
         
- Identification vendeur<br/>
                      ```seller```
      Un vendeur a un menu personnalisé, il peut  ajouter des articles en fonction de son stock ou encore effectuer des promotions sur certains produit.
       _exemple: Entrez votre numéro de compte: seller_<br/>
- Identification administrateur<br/>
                      ```admin```
      L'administrateur quant à lui gère tout le back-end c'est à dire il peut refresh la base de donnée, inserer ses propres requêtes ou encore inserer des listes de requetes d'insertion comme 'Insert_OK'.              <br/>
      _exemple: Entrez votre numéro de compte: admin_
      
 #### Menu client & introduction des fonctionnalités</br>    
 
 ![image](https://user-images.githubusercontent.com/58702474/117142302-d1763880-adaf-11eb-85ad-ce25e9d8b16b.png)

  L'objectif de cette partie est de montrer les principales fonctionnalitées de l'application <br/>
   <br/>
 - Les articles
    <br/>
    ![image](https://user-images.githubusercontent.com/58702474/117142645-392c8380-adb0-11eb-81ec-50c485396d7b.png)
    <br/>
    En navigant sur la page article on a tout les articles présents sur la base de données même ceux qui sont indisponible.
    <br/>
     <br/>
 - Les types d'articles<br/>
    ![image](https://user-images.githubusercontent.com/58702474/117143457-28c8d880-adb1-11eb-9ef8-46d25172c682.png)
    <br/>
    Les types articles sont le résultat de la view de type article c'est à dire qu'on a assez à toutes les informations utiles pour décrire un produit.
    <br/>
     <br/>
 - Effectuer une commande <br/>
    ![image](https://user-images.githubusercontent.com/58702474/117143780-7ba29000-adb1-11eb-9134-a64be144ee2d.png)
    <br/>
    
    Lorsque l'on souhaite commander on a un panier qui affiche tout les articles qu'on a pris avec le total en €. Ce panier se met à jour en temps réel et on peut supprimer des articles quand on souhaite.
    <br/>
     <br/>
 - Mes commandes <br/>
   ![image](https://user-images.githubusercontent.com/58702474/117144309-13a07980-adb2-11eb-9bc8-a673a110c8d0.png)
    <br/>
    On affiche ici toutes les dernieres commandes trié de la plus ancienne à la plus récente (en suivant l'ordre de la console python).
    De plus on peut avoir les informations des dernieres commandes (appuyez sur i).
    <br/>
    ![image](https://user-images.githubusercontent.com/58702474/117145051-f91ad000-adb2-11eb-9c30-803b15fc7fa6.png)
    <br/>
     <br/>
       
