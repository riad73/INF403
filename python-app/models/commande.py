class Commande:
  def __init__(self, numero_commande, numero_client, adresse_livraison, date_achat, statut):
    self.numero_commande = numero_commande
    self.numero_client = numero_client
    self.adresse_livraison = adresse_livraison
    self.date_achat = date_achat
    self.statut = statut
