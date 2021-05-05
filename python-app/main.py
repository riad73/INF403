#!/usr/bin/python3
from utils import db
from models.client import Client
from models.article import Article
from models.type_article import TypeArticle
from models.commande import Commande
from models.view_type_article import ViewTypeArticle
from beautifultable import BeautifulTable
from pyfiglet import Figlet
from termcolor import colored
from datetime import datetime
import random


client = Client(0, "", "", "")
isConnected = False
isSeller = False
isAdmin = False


def select_tous_les_articles(conn):
    """
    Affiche la liste de tous les bateaux.

    :param conn: Connexion à la base de données
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM Articles")

    rows = cur.fetchall()
    count = 0

    table = BeautifulTable()
    table.columns.header = ["Ref", "Articles", "Prix (€)"]
    for row in rows:
        article: Article = Article(row[0], row[1], row[2], row[3])
        cur.execute("SELECT * FROM TypeArticles WHERE nom_article=?", (article.nom_article,))
        row = cur.fetchall()
        type_article = TypeArticle(row[0][0], row[0][1])

        table.rows.append([article.reference_article, article.nom_article, str(type_article.prix)])

        count += 1

    print(table)
    print("TOTAL D'ARTICLES: ", count)
    print("+---------------------------------------------------------+")


def afficher_tout_les_client(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM Clients")

    rows = cur.fetchall()
    for row in rows:
        print(row)


def select_tous_les_articles_dispo(conn):
    print("+------------------ ARTICLES DISPONIBLES ------------------+")
    cur = conn.cursor()
    cur.execute("SELECT * FROM Articles WHERE disponible='TRUE'")

    rows = cur.fetchall()
    count = 0
    table = BeautifulTable()
    table.columns.header = ["Ref", "Articles", "Prix (€)"]
    for row in rows:
        article: Article = Article(row[0], row[1], row[2], row[3])
        cur.execute("SELECT * FROM TypeArticles WHERE nom_article=?", (article.nom_article,))
        row = cur.fetchall()
        type_article = TypeArticle(row[0][0], row[0][1])

        table.rows.append([article.reference_article, article.nom_article, str(type_article.prix)])


        count += 1

    print(table)
    print("TOTAL D'ARTICLES DISPONIBLES: ", count)
    print("+---------------------------------------------------------+")


def update_articles_commandes(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM Articles JOIN Paniers USING(reference_article)")
    rows = cur.fetchall()
    for row in rows:
        if row[4] == 'TRUE':
            conn.cursor().execute("UPDATE Articles SET disponible = 'FALSE' WHERE reference_article = ?", (row[0],))
        else:
            conn.cursor().execute("UPDATE Articles SET disponible = 'TRUE' WHERE reference_article = ?", (row[0],))
    print('✓')
    conn.commit()


def chercher_client(conn, uid):
    global isConnected, client, isSeller, isAdmin
    if str(uid) == "seller":
        isSeller = True
        return "q"
    elif str(uid) == "admin":
        isAdmin = True
        return "q"
    else:
        cur = conn.cursor()
        cur.execute("SELECT * FROM Clients WHERE numero_client = ?", (uid,))
        rows = cur.fetchall()
        count = 0
        for row in rows:
            count += 1

        if count == 0:
            print("Vous n'êtes pas enregistré. ")
            user_input = input('Voulez vous en créer un compte ? O/N: ')
            if user_input == 'O':
                creer_client(conn)
                return "q"
            else:
                return "n"
        else:
            client = Client(rows[0][0], rows[0][1], rows[0][2], rows[0][3])
            print("")
            print("Connexion réussite ✓")
            print("Heureux de vous revoir " + client.prenom + " !")
            isConnected = True
            return "q"


def creer_client(conn):
    global isConnected, client
    nom = input('Entrez votre nom: ')
    prenom = input('Entrez votre prénom: ')
    adresse = input('Entrez votre adresse: ')

    cur = conn.cursor()
    cur.execute("SELECT numero_client FROM Clients")
    rows = cur.fetchall()
    liste = []
    for row in rows:
        liste.append(row[0])

    id = generate_random_id(conn, "uid")

    cur = conn.cursor()
    cur.execute("""INSERT INTO Clients VALUES(?,?,?,?)""", (str(id), nom, prenom, adresse))
    conn.commit()
    print("")
    print("Création du compte ✓")
    print(colored("Enregistez votre numéro client pour vous connecter ultérierement", 'red'))
    print("Numéro client: " + str(id))
    print("Bienvenue " + prenom + " !")
    client = Client(id, nom, prenom, adresse)
    isConnected = True


def mes_commandes(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM Commandes_View WHERE numero_client = ? ORDER BY date_achat", (client.numero_client,))
    print("Voici vos dernieres commandes : ")
    rows = cur.fetchall()
    count = 0
    table = BeautifulTable()
    table.columns.header = ["N°Commande", "Livrée à" , "Acheté le", "Statut", "Nb Article(s)"]

    for row in rows:
        table.rows.append([str(row[0]), str(row[2]), str(row[3]), row[4], row[5]])
        count += 1
    print(table)
    print("nombre total de commande: ", count)
    user_input = 'a'

    print("[i] pour plus d'information sur un commande      [q] pour quitter")
    while user_input != 'q':
        if user_input == 'i':
            numero_input = input('Entrez le numéro de votre commande: ')
            chercher_commande(conn, numero_input)
        user_input = input('Tapez ici: ')


def chercher_commande(conn, numero):
    cur = conn.cursor()
    panier = []
    cur.execute("SELECT reference_article FROM Paniers WHERE numero_commande = ?", (numero,))
    rows = cur.fetchall()
    for row in rows:
        panier.append(row[0])

    liste_type_articles=[]
    chercher_panier(conn, panier, liste_type_articles)
    total = 0
    table = BeautifulTable()
    table.columns.header = ["Ref", "Article", "Prix (€)"]
    for i in range(0, len(liste_type_articles)):
        type_article: TypeArticle = liste_type_articles[i]
        table.rows.append([str(panier[i]), type_article.nom_article, str(type_article.prix)])
        total += type_article.prix
    print(table)
    print("TOTAL:      " + str(total) + "€")


def passer_commande(conn):
    print(colored("Pour passer une commande veuillez taper la référence de l'article", 'red'))
    print("Veuillez choisir des articles parmi la liste suivante: ")
    cur = conn.cursor()
    cur.execute("SELECT * FROM Articles WHERE disponible='TRUE'")
    select_tous_les_articles_dispo(conn)
    liste = []
    rows = cur.fetchall()
    for row in rows:
        liste.append(row[0])

    panier = []

    user_input = input('Ajoutez un article ( Q quitter ): ')
    quitter = False
    while user_input != 'C':
        if user_input.isdigit() and estDansListe(liste, int(user_input)):
            liste.remove(int(user_input))
            panier.append(int(user_input))
        elif user_input == 'V':
            select_tous_les_articles_dispo(conn)
        elif user_input == 'S':
            if len(panier) != 0:
                inputS = input('Pour supprimer entrez la référence de votre article (1ere colonne): ')
                if inputS.isdigit() and estDansListe(panier, int(inputS)):
                    ref = int(inputS)
                    panier.remove(ref)
            else:
                print("❌ Opération impossible. Votre panier est vide.")

        elif user_input.isdigit() and estDansListe(panier, int(user_input)):
            print("Vous ne pouvez pas commander deux fois la même référence d'article.")

        else:
            print("L'article saisi est indisponible.")

        if len(panier) != 0:
            print("\n         VOTRE PANIER  \n")
            liste_type_articles = []
            chercher_panier(conn, panier, liste_type_articles)
            total = 0
            table = BeautifulTable()

            table.columns.header = ["Ref", "Article", "Prix (€)"]
            for i in range(0, len(liste_type_articles)):
                type_article: TypeArticle = liste_type_articles[i]
                table.rows.append([str(panier[i]), type_article.nom_article, str(type_article.prix)])
                total += type_article.prix
            print(table)
            print("TOTAL:      " + str(total) + "€")

        if user_input == 'Q':
            quitter = True
            user_input = 'C'
        else:
            user_input = input('Ajoutez un article (S supprimer | C commander | Q quitter ): ')

    if not quitter:
        cur = conn.cursor()
        cur.execute("SELECT numero_commande FROM Commandes")
        rows = cur.fetchall()
        liste = []
        for row in rows:
            liste.append(row[0])
        inputA = "b"
        adresse = client.adresse
        annuler = False
        while inputA != 'a':
            print("[m] se faire livrer chez moi | [o] autre | [q] annuler")
            inputA = input('Tapez ici: ')
            if inputA.lower() == 'm':
                inputA = 'a'
            elif inputA.lower() == 'o':
                adresse = input('Veuillez saisir votre adresse de livraison: ')
                inputA = 'a'
            elif inputA.lower() == 'q':
                annuler = True
                inputA = 'a'
            else:
                print("Erreur ❌: Option entrée inconnu ")
                inputA = input('Saisissez une option ici: ')

        if annuler or user_input == 'Q':
            print("Annulation de la commande prise en compte ✓")
            panier.clear()
            print("[a] Les articles                 [b] Les articles disponibles")
            print("[c] Effectuer une commande       [d] Mes commandes")
            print("[e] Les type d'articles          [f] Supprimer une commande")
            print("                     [q] quitter")

        if len(panier) != 0:
            print("Achat en cours...")
            cur = conn.cursor()
            statut = "expediee"
            id = generate_random_id(conn, "cid")
            date = datetime.today().strftime('%Y-%m-%d')
            cur.execute("""INSERT INTO Commandes VALUES(?,?,?,?,?)""",
                        (id, client.numero_client, adresse, date, statut))

            for i in panier:
                cur = conn.cursor()
                cur.execute("""INSERT INTO Paniers VALUES(?,?)""", (id, int(i)))

            update_articles_commandes(conn)
            print("Merci pour votre achat !")
            conn.commit()
            mes_commandes(conn)
    else:
        panier.clear()
        print("[a] Les articles                 [b] Les articles disponibles")
        print("[c] Effectuer une commande       [d] Mes commandes")
        print("[e] Les type d'articles          [f] Supprimer une commande")
        print("                     [q] quitter")


def chercher_panier(conn, liste, liste_type_articles):
    cur = conn.cursor()
    for ref in liste:
        cur.execute("SELECT * FROM Articles WHERE reference_article=?", (ref,))
        row = cur.fetchall()
        article = Article(ref, row[0][1], row[0][2], row[0][3])
        cur.execute("SELECT * FROM TypeArticles WHERE nom_article=?", (article.nom_article,))
        row = cur.fetchall()
        type_article = TypeArticle(row[0][0], row[0][1])
        liste_type_articles.append(type_article)


def estDansListe(liste, ref):
    for i in liste:
        if i == ref:
            print("Dans liste")
            return True
    return False


def supprimer_commande(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM Commandes_View WHERE numero_client = ? ", (client.numero_client,))
    print("Voici vos dernieres commandes : ")
    rows = cur.fetchall()
    count = 0
    table = BeautifulTable()
    table.columns.header = ["N°Commande", "Livrée à", "Acheté le", "Statut", "Nb Article(s)"]

    for row in rows:
        table.rows.append([str(row[0]), str(row[2]), str(row[3]), row[4], row[5]])
        count += 1
    print(table)
    print("nombre total de commande: ", count)

    num = input("Pour supprimer une commande entrez son n° de commande: ")
    cur.execute("DELETE FROM Commandes WHERE numero_commande = ?", str(num))
    cur.execute("DELETE FROM Paniers WHERE numero_commande = ? ", str(num))
    conn.commit()
    update_articles_commandes(conn)


def update_statut_commande(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM Commandes")
    rows = cur.fetchall()
    for row in rows:
        commande = Commande(row[0], row[1], row[2], row[3], row[4])
        date_time_str = commande.date_achat
        date_time_obj = datetime.strptime(date_time_str, '%Y-%m-%d')
        date = datetime.now()
        delta = date_time_obj - date
        day = delta.days
        day = abs(day)

        if day <= 1 and commande.statut != "livree":
            conn.cursor().execute("UPDATE Commandes SET statut = 'expediee' where numero_commande = ?",
                                  (commande.numero_commande,))
        elif 1 < day < 3 and commande.statut != "transit":
            conn.cursor().execute("UPDATE Commandes SET statut = 'transit' where numero_commande = ?",
                                  (commande.numero_commande,))
        elif commande.statut != "livree":
            conn.cursor().execute("UPDATE Commandes SET statut = 'livree' where numero_commande = ?",
                                  (commande.numero_commande,))
        conn.commit()


def select_les_different_types_articles(conn):
    print("+------------------ LES TYPES D'ARTICLES------------------+")
    cur = conn.cursor()
    cur.execute("SELECT * FROM TypeArticles_View")
    rows = cur.fetchall()
    table = BeautifulTable()
    table.columns.header = ["Nom d'article", "Prix (€)", "STOCK", "DISPONIBILITES"]
    for row in rows:
        ViewTA = ViewTypeArticle(row[0], row[1], row[2])
        cur2 = conn.cursor()
        cur2.execute("SELECT COUNT(nom_article) FROM Articles WHERE (disponible = 'FALSE' AND nom_article = ?)", (ViewTA.nom_article,))
        cnt = cur2.fetchall()
        dispo = ViewTA.stock - cnt[0][0]

        if dispo > 0:
            table.rows.append([ViewTA.nom_article, ViewTA.prix, ViewTA.stock, dispo])
        else:
            table.rows.append([ViewTA.nom_article, ViewTA.prix, ViewTA.stock, "RUPTURE DE STOCK"])
    print(table)
    print("+---------------------------------------------------------+")


def ajouter_article(conn):
    nom_a = input("Entrez le nom d'article: ")
    prix = input("Entrez son prix: ")
    quantite = input("Entrez un stock: ")
    cur = conn.cursor()
    while not quantite.isdigit():
        quantite = input("Entrez un stock: ")
    cur.execute("""INSERT INTO TypeArticles VALUES(?,?)""", (nom_a, str(prix)))
    liste_allee = ["A", "B", "C", "D", "E", "F", "G"]
    allee = random.choice(liste_allee)
    print("Vous inquitez pas on s'occupe de tout !")
    print("Génération des articles dans le catalogue...")
    for i in range(0, int(quantite)):
        rid = generate_random_id(conn, "rid")
        #Random emplacement
        cur2 = conn.cursor()
        cur2.execute("SELECT place FROM Entrepot WHERE allee = ?", allee)
        rows = cur2.fetchall()
        liste = []
        for row in rows:
            liste.append(row[0])
        place = 1
        while place in liste:
            place = random.randrange(1, 500)
        cur.execute("""INSERT INTO Entrepot VALUES(?,?, "23 Rue des iles")""", (allee, str(place)))
        cur.execute("""INSERT INTO Articles VALUES(?,?,?,?, "TRUE")""", (rid, nom_a, allee, str(place)))

    print("Insertion prise en compte 😀")
    conn.commit()


def generate_random_id(conn, type):
    alea = random.randrange(1, 10000, 1)
    liste =[]
    if type == "uid":
        cur = conn.cursor()
        cur.execute("SELECT numero_client FROM Clients")
        rows = cur.fetchall()
        liste = []
        for row in rows:
            liste.append(row[0])

    elif type == "cid":
        cur = conn.cursor()
        cur.execute("SELECT numero_commande FROM Commandes")
        rows = cur.fetchall()
        liste = []
        for row in rows:
            liste.append(row[0])
    elif type == "rid":
        cur = conn.cursor()
        cur.execute("SELECT reference_article FROM Articles")
        rows = cur.fetchall()
        liste = []
        for row in rows:
            liste.append(row[0])

    while alea in liste:
        alea = random.randrange(1, 10000, 1)
    return alea


def promotion(conn):
    nom_article = input("Entrez le nom de l'article: ")
    remise = input("Entrez la remise entre (ex 10% = 0.1): ")
    remise = 1 - float(remise)
    conn.cursor().execute("UPDATE TypeArticles SET prix = (?) * prix WHERE nom_article = ?", (str(remise), nom_article))
    conn.commit()


def commande_sql(conn):
    cur = conn.cursor()
    query = input("Entrez votre requete ici: ")
    veuxParam = input("Vous avez des paramètres ? O/N")
    if veuxParam == 'O':
        param = input("Entrez des paramètres: ")
        print("Execution.")
        cur.execute(query, param)
    else:
        print("Execution.")
        cur.execute(query)

    cur.execute(query)
    view_rows = input("Voir les rows? O/N")
    rows = cur.fetchall()
    if view_rows =='O':
        for row in rows:
            print(row)


def main():
    global isConnected, client, isSeller, isAdmin
    # Nom de la BD à créer
    db_file = "data/boutique.db"

    conn = db.creer_connexion(db_file)

    print("\n")
    f= Figlet(font='standard')
    print(colored(f.renderText('MyMarket'), 'blue'))
    print("\n Mise à jour articles commandés", end=' ')
    update_articles_commandes(conn)
    update_statut_commande(conn)
    if not isConnected:
        f = Figlet(font='banner3-d')
        print(colored(f.renderText('Accueil')))
        print("")
        print()
        print("[c] se connecter      [i] s'inscrire      [q] quitter")
        user_input = input('Tapez ici: ')
        while user_input != 'q':
            if user_input == 'c':
                print("[Identification]")
                user_input = input('Entrez votre numéro de compte: ')
                user_input = chercher_client(conn, user_input)

            elif user_input == 'i':
                print("[Création d'un compte client]")
                creer_client(conn)
                user_input = 'q'
            else:
                print("Erreur ❌")
                print("[c] se connecter      [i] s'inscrire      [q] quitter")
                user_input = input('Tapez ici: ')

    print("")
    if isConnected:
        f = Figlet(font='banner3-d')
        print(colored(f.renderText('Menu')))
        print("[a] Les articles                 [b] Les articles disponibles")
        print("[c] Effectuer une commande       [d] Mes commandes")
        print("[e] Les type d'articles          [f] Supprimer une commande")
        print("                     [q] quitter")
        user_input = input('Tapez ici: ')
        print("")
        while user_input != "q":
            if user_input == 'a':
                print("Liste de tous les articles:")
                select_tous_les_articles(conn)
            elif user_input == 'b':
                print("Tous les articles disponibles:")
                select_tous_les_articles_dispo(conn)
            elif user_input == 'c':
                passer_commande(conn)
            elif user_input == 'd':
                mes_commandes(conn)
            elif user_input == 'e':
                select_les_different_types_articles(conn)
            elif user_input == 'f':
                supprimer_commande(conn)
            elif user_input == 'm':
                print("[a] Les articles                 [b] Les articles disponibles")
                print("[c] Effectuer une commande       [d] Mes commandes")
                print("[e] Les type d'articles          [f] Supprimer une commande")
                print("                     [q] quitter")
            else:
                print("Erreur ❌: Commande entrée inconnu ")
            user_input = input('Tapez ici ([m] pour afficher le menu): ')
        print("Au revoir " + client.prenom)


    if isSeller:
        f = Figlet(font='banner3-d')
        print(colored(f.renderText('Seller Panel'), "blue"))

        print("[a] Ajouter des articles  [b] Promotions")
        print("[q] quitter                         ")

        user_input = input('Tapez ici: ')
        while user_input != "q":
            if user_input == "a":
                print("Ajouter un article")
                ajouter_article(conn)
            elif user_input == "b":
                print("Promotion")
                promotion(conn)
            elif user_input == "m":
                print("[a] Ajouter des articles  [b] Promotions")
                print("[q] quitter")
            else:
                print("Erreur ❌: Commande entrée inconnu ")
            user_input = input('Tapez ici ([m] pour afficher le menu): ')

    if isAdmin:
        f = Figlet(font='banner3-d')
        print(colored(f.renderText('Admin Panel'), "blue"))
        print("[a] CREER LA DB                  [b] INSERER LISTE ARTICLES OK")
        print("[c] EXECUTER DES COMMANDES SQL   [m] MENU")
        print("                         [q] quitter")
        user_input = input('Tapez ici: ')
        while user_input != "q":
            if user_input == "a":
                db.mise_a_jour_bd(conn, "data/boutique_creation.sql")
            elif user_input == "b":
                db.mise_a_jour_bd(conn, "data/boutique_inserts_ok.sql")
            elif user_input == "c":
                commande_sql(conn)
            elif user_input == "m":
                print("[a] CREER LA DB                  [b] INSERER LISTE ARTICLES OK")
                print("[c] EXECUTER DES COMMANDES SQL   [m] MENU")
                print("                         [q] quitter")
            else:
                print("Erreur ❌: Commande entrée inconnu ")
            user_input = input('Tapez ici ([m] pour afficher le menu): ')

    isConnected = False
    isAdmin = False
    isSeller = False
    main()


if __name__ == "__main__":
    main()


