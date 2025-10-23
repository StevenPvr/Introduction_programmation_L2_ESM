

# Déjà quelques connaissances en bibliothèque - arborescence de projet - fonction - classe - log - docstrings - test unitaire, e2e - API etc. Mais je n'ai jamais écrit des lignes de code, c'est donc la première fois ici (oui j'ai fait les choses à l'envers, l'époque rend cela tentant).


from datetime import datetime

# Création (ou écrasement) du fichier de résultats
fichier_resultats = open("TP2/resultats_tp2.txt", "w", encoding="utf-8")

# Fonction utilitaire : écrit à l'écran et dans le fichier
def log(texte):
    print(texte)
    fichier_resultats.write(str(texte) + "\n")

log("=== Résumé des exercices du TP2 ===")
log("Exécuté le : " + str(datetime.now()))
log("")  # ligne vide

# Exercice 1 - Création d'une liste

prenom = ["Emma", "Noah", "Chloé", "Clément", "Liam"]

log("Ex1 Premier et dernier : " + prenom[0] + ", " + prenom[-1])

# Manipulations sur la liste des prénoms
add_prenom = prenom.append("Theo") # Ajoute "Theo" à la fin de la liste prenom.

print(prenom)

delete_prenom = prenom.remove("Chloé") # Supprime "Chloé" de la liste prenom.

print(prenom)

trie_prenom = prenom.sort() # Trie la liste prenom par ordre alphabétique.

print(prenom)

len(prenom)  # Renvoie le nombre d'éléments dans la liste prenom.    

# Recherche de l'index d'un prénom
if ("Alice" in prenom):
    print(prenom.index("Alice"))  # Renvoie l'index de "Alice" dans la liste prenom si elle s'y trouve. Sinon, une erreur est renvoyée.
else:
    print("Alice n'est pas dans la liste prenom.")


# Exercice 2 - Moyenne de notes

notes = [13, 20, 3, 9, 16]

# Calcul de la moyenne des notes
moyenne = sum(notes) / len(notes) # Calcule la moyenne des notes dans la liste.

log("Ex2 Moyenne des notes : " + str(round(moyenne, 1))) # Affiche la moyenne des notes en arrondissant.

print([note for note in notes if note > moyenne])

# Calcul des notes minimales et maximales
note_extrema = (min(notes), max(notes)) # Calcule les notes minimales et maximales.
print(f"Note min: {note_extrema[0]}, Note max: {note_extrema[1]}") # Affiche les notes minimales et maximales.

# Calcul de l'écart-type
ecart_type = (sum((note - moyenne) ** 2 for note in notes) / len(notes)) ** 0.5

print(f"Ecart-type des notes: {ecart_type}") # Affiche l'écart-type des notes.


# Exercice 3 - Noms en majuscules

noms_maj = ["ALICE", "bob", "CHARLIE", "dave", "EVE"]

# Affiche uniquement les prénoms entièrement en majuscules
log("Ex3 Prénoms en majuscules :")
for nom in noms_maj:
    if nom.isupper():
        print(nom)

# Met à jour la liste pour que tous les prénoms soient en majuscules
noms_maj = [nom.upper() for nom in noms_maj]
print(f"\nNouvelle liste noms_maj: {noms_maj}")

# Affiche uniquement les prénoms commençant par A (insensible à la casse)
print("\nPrénoms commençant par A:")
for nom in noms_maj:
    if nom.upper().startswith("A"):
        print(nom)

# Donne la longueur de chaque prénom
print("\nLongueur de chaque prénom:")
longueurs = []
for nom in noms_maj:
    longueur = len(nom)
    print(f"{nom}: {longueur} caractères")
    longueurs.append(longueur)

# Trouve le prénom le plus long
longueurs_max = max(longueurs)
index_max = longueurs.index(longueurs_max)
print(f"Le prénom le plus long est {noms_maj[index_max]} avec {longueurs_max} caractères.")

# Exercice 4 - Liste de carrés

# Affiche la liste des carrés des nombres de 1 à 10
print("\nListe des carrés des nombres de 1 à 10:")
carres = []
for i in range (1, 11):
    carres.append(i**2)
    print(f"Carré de {i}: {i**2}")

# Filtre les carrés pour ne garder que ceux qui sont pairs
carres = [c for c in carres if c % 2 == 0]

# Calcule la somme des carrés pairs
somme_carres_pairs = sum(carres)

log("Ex4 Somme des carrés pairs : " + str(somme_carres_pairs))

# Exercice 5 - Dictionnaire simple

etudiants = {"nom": "Alice", "age": 22, "notes": 14}

log("Ex5 Nom et note : " + etudiants["nom"] + ", " + str(etudiants["notes"]))

# Ajouter un point à la note de l'étudiant
etudiants["notes"] += 1
print("Nouvelle note:", etudiants["notes"])

# Marquer l'étudiant comme présent
etudiants["present"] = True 
print("present:", etudiants["present"])

# Lecture d'une clé absente avec une valeur par défaut grâce à get()
cle_absente = etudiants.get("cle", "defaut")
if cle_absente == "defaut":
    print("La clé 'cle' est absente du dictionnaire.")


# Exercice 6 - Liste de dictionnaires

etudiants = [
    {"nom": "Sophia", "notes": [14, 15, 13]},
    {"nom": "Clement", "notes": [10, 12, 11]},
    {"nom": "Katarina", "notes": [16, 12, 14]}
]

for etudiant in etudiants:
    etudiant["moyenne"] = sum(etudiant["notes"]) / len(etudiant["notes"])
    log("Ex6 " + etudiant['nom'] + " a une moyenne de " + str(round(etudiant['moyenne'], 1)))

print("\nClassement des étudiants par moyenne décroissante:")

# Tri des étudiants par moyenne décroissante, puis par nom alphabétiquement en cas d'égalité
classement = sorted(
    etudiants,
    key=lambda x: (- round(x["moyenne"], 1), x["nom"].lower())
)

# Affichage du classement avec indication des égalités
prev_moyenne = None
for rang, etudiant in enumerate(classement, start=1):
    moyenne = round(etudiant["moyenne"], 1)
    msg = f"{rang}. {etudiant['nom']} a une moyenne de {moyenne}"
    if moyenne == prev_moyenne: # Comme les moyennes sont classées dans l'ordre décroissant, on peut juste comparer avec la moyenne précédente pour savoir s'il y a une égalité.
        msg += " (même moyenne que le précédent)"
    print(msg)
    prev_moyenne = moyenne 

# Exercice 7 - Comptage de mots

import string

phrase = input("Entrez une phrase: ")

# Conversion de la phrase en minuscules. Remarque : on aurait pu faire cela directement dans l'input avec .lower()
phrase_lower = phrase.lower()
print(phrase_lower)

# Suppression de la ponctuation
for char in string.punctuation:
    phrase_lower = phrase_lower.replace(char, "")

print(phrase_lower)

# Séparation de la phrase en mots
mots_split = phrase_lower.split()
print(mots_split)

dictionnaire = {}

# Comptage des occurrences de chaque mot
for mot in mots_split:
    if mot in dictionnaire:
        dictionnaire[mot] += 1
    else:
        dictionnaire[mot] = 1

log("Ex7 Comptage des mots : " + str(dictionnaire))

# Exercice 8 - Fusion de dictionnaires

p1 = { " pomme " : 2 , " pain " : 1 , " riz " : 1}
p2 = { " pomme " : 1 , " yaourt " : 4 , " riz " : 2}

p_total = p1.copy() # On crée une copie de p1 pour ne pas modifier le dictionnaire d'origine.

for cle, valeur in p2.items(): # Permet de récupérer les clés + la valeur associée dans le dictionnaire p2.
    if cle in p_total:        # Si la clé existe déjà dans le dictionnaire fusionné, on ajoute la valeur.
        p_total[cle] += valeur
    else:
        p_total[cle] = valeur # Sinon, on crée une nouvelle entrée dans le dictionnaire fusionné avec la valeur de p2.

log("Ex8 Fusion des courses : " + str(p_total))

print("\nDictionnaire trié par quantité décroissante:")
p_total_trié = sorted(p_total.items(), key=lambda x: x[1], reverse=True) # sorted() permet de renvoyer une nouvelle liste. L'argument reverse=True permet de trier par ordre décroissant.

print(p_total_trié)


# Exercice 9 - Fréquence des lettres

mot = input("Entrez un mot: ").lower() # Cette fois-ci on convertit directement l'input en minuscules.

print(mot)

for caractere in mot:
    if caractere.isalpha():  # On vérifie que le caractère est bien une lettre afin de ne pas compter les espaces ou autres caractères spéciaux, chiffres, etc.
        if caractere in dictionnaire:
            dictionnaire[caractere] += 1
        else:
            dictionnaire[caractere] = 1

log("Ex9 Fréquence des lettres : " + str(sorted(dictionnaire.items(), key=lambda x: x[1], reverse=True)))  # Trie le dictionnaire par fréquence décroissante des lettres.

# Exercice 10 - Classement de notes

valeurs = {"Alice": 14, "Bob": 10, "Clara": 16}

nom_tries = sorted(valeurs, key=lambda x: valeurs[x], reverse=True) # Trie les noms des étudiants par ordre décroissant de leurs notes.
print(nom_tries)
log("Ex10 " + nom_tries[0] + " est la meilleure note, " + nom_tries[-1] + " est la moins bonne note") # Affiche le nom de l'étudiant avec la meilleure et la moins bonne note.

# Exercice 11 - Inventaire simple (prix et stock)

inventaire = {
"pomme" : { "prix" : 0.5 , "stock" : 20} ,
"pain" : { "prix" : 1.2 , "stock" : 10} ,
"riz" : { "prix" : 2.0 , "stock" : 5}
}

valeur_totale = sum(item["prix"] * item["stock"] for item in inventaire.values()) # Calcule la valeur totale de l'inventaire en multipliant le prix par le stock pour chaque article, puis en additionnant ces valeurs.
log("Ex11 Valeur totale de l'inventaire : " + str(valeur_totale))

limite = {"pomme": 10, "riz": 5}
commande = {"pomme": 3, "riz": 2}

total_commande = 0 # Initialise le total de la commande à 0.

for produit, details in inventaire.items():
    nom = produit.lower()
    if nom in limite and details["stock"] >= limite[nom]: # Vérifie si le produit est dans la liste des limites et respecte la condition de stock.
        print(f"Le produit {produit} est disponible dans ces quantités, ({details['stock']} unités restantes).")


        if nom in commande and commande[nom] <= details["stock"]: # On vérifie si la commande est possible. 
            total_commande += commande[nom] * details["prix"] # Calcule le total de la commande en multipliant la quantité commandée par le prix unitaire.
            details["stock"] -= commande[nom]  # Met à jour le stock après la commande.
            print(f"Commande de {commande[nom]} unités de {produit} passée.")

    elif nom in ("pomme", "riz") and details["stock"] < limite[nom]: # Si la condition n'est pas remplie, alors on ne vends pas les produits.
        print(f"Attention, le stock de {produit} n'est pas suffisant ({details['stock']} unités restantes, pas de vente possible).")

print(f"Total de la commande: {total_commande}€")
print("Stock mis à jour:", inventaire)

if "riz" in inventaire:
    inventaire["riz"]["prix"] *= 0.9  # Réduction de 10% du prix du riz.
    print("Remise de 10% appliquée sur le prix du riz")

valeur_totale = sum(item["prix"] * item["stock"] for item in inventaire.values()) # Recalcule la valeur totale de l'inventaire après mise à jour du stock.
print(f"Nouvelle valeur totale de l'inventaire: {valeur_totale}")

# Exercice 12 - Petites "stats" sur transactions

tx = [
    {"nom": "Alice", "montant": 12.5},
    {"nom": "Bob", "montant": 7.0},
    {"nom": "Alice", "montant": 3.5},
    {"nom": "Clara", "montant": 20.0}
]

dictionnaire = {}

# Agrégation des montants par nom
for transaction in tx:
    nom = transaction["nom"]
    montant = transaction["montant"]
    
    # Mise à jour du dictionnaire avec le montant total par nom
    if nom in dictionnaire:
        dictionnaire[nom] += montant
    else:
        dictionnaire[nom] = montant

log("Ex12 Agrégation transactions : " + str(sorted(dictionnaire.items(), key=lambda x: x[1], reverse=True)))  # Trie le dictionnaire par montant total décroissant.

# Exercice 13 - Fonctions utilistaires (liste de nombres). Utilisation d'une class, des docstrings et du logging afin d'avoir un code plus propre et réutilisable.

import logging
logging.basicConfig(level=logging.INFO)

nombres = [13, 20, 3, 9, 16, 13, 9, 3, 16, 20, 13, 9, 3, 16]

# Création d'une classe afin d'englober toutes les fonctions
class BasicStats:
    """
    Idée: je centralise mes petites fonctions stats dans une classe.
    Comme ça je passe la liste une seule fois au départ et je la réutilise partout.
    """

    # Permet de passer la liste de nombres à chaque fonction dans la classe sans avoir à la redéfinir à chaque fois.
    def __init__(self, nombres):
        """Je fixe la liste de travail ici."""
        self.nombres = list(nombres)

    # Fonction pour calculer la moyenne d'une liste de nombres
    def moyenne_liste(self):
        """
        But: moyenne simple (somme / taille).
        Si la liste est vide, je log l’erreur et je renvoie None pour signaler le cas.
        """
        if not self.nombres:
            logging.error("La liste est vide")
            return None
        moyenne = sum(self.nombres) / len(self.nombres)
        logging.info(f"Moyenne calculée: {moyenne}")
        return moyenne

    # Appel de la fonction : Mais ici on appelera tout à la fin sinon il n'y a plus d'accès à la liste.
    # resultat = moyenne_liste(nombres)
    # logging.info(f"La moyenne des nombres est: {resultat}")

    # Fonction pour calculer la médiane d'une liste de nombres
    def mediane_liste(self):
        """
        But: médiane.
        - Si n impair: je prends l’élément du milieu.
        - Si n pair: je fais la moyenne des deux valeurs du centre.
        Le tri est indispensable pour savoir quelles sont les valeurs centrales.
        """
        if not self.nombres:
            logging.error("La liste est vide")
            return None
        liste_triee = sorted(self.nombres)  # Trie la liste du plus petit au plus grand
        milieu = len(self.nombres) // 2

        if len(self.nombres) % 2 == 1:  # impair
            mediane = liste_triee[milieu]
        else:  # pair
            mediane = (liste_triee[milieu - 1] + liste_triee[milieu]) / 2

        logging.info(f"Médiane calculée: {mediane}")
        return mediane

    # Fonction afin de calculer le mode d'une liste de nombres
    def mode_liste(self):
        """
        But: mode(s) = valeur(s) la/les plus fréquente(s).
        Je compte les occurrences à la main pour montrer la mécanique.
        S’il y a égalité sur la fréquence max, je renvoie toutes les valeurs concernées.
        """
        if not self.nombres:
            logging.error("La liste est vide")
            return None

        frequence = {}
        for nombre in self.nombres:  # Compte la fréquence de chaque nombre
            if nombre in frequence:
                frequence[nombre] += 1
            else:
                frequence[nombre] = 1

        maxf = max(frequence.values())
        modes = sorted([val for val, f in frequence.items() if f == maxf])  # tri pour un rendu stable

        # Si une seule valeur atteint la fréquence max, je rends le nombre; sinon je rends la liste des valeurs ayant la même fréquence.
        res = modes[0] if len(modes) == 1 else modes
        logging.info(f"Mode(s) calculé(s): {res} (fréquence max = {maxf})")
        return res

# Appels des fonctions
stats = BasicStats(nombres)
moyenne = stats.moyenne_liste()
mediane = stats.mediane_liste()
mode = stats.mode_liste()

log("Ex13 Moyenne=" + str(moyenne) + ", Médiane=" + str(mediane) + ", Mode=" + str(mode))
logging.info(f"Calcul des statistiques basiques terminé: Moyenne={moyenne}, Médiane={mediane}, Mode={mode}")

# Ma première classe Python écrite à la main !


# Exercice 14 - Groupements simples (sans pandas)

catalogue = [
    {"categorie": "Fruits", "produit": "Pomme", "prix": 0.5},
    {"categorie": "Fruits", "produit": "Banane", "prix": 0.3},
    {"categorie": "Fruits", "produit": "Mangue", "prix": 1.8},
    {"categorie": "Boissons", "produit": "Eau", "prix": 0.7},
    {"categorie": "Boissons", "produit": "Jus d'orange", "prix": 2.5},
    {"categorie": "Boissons", "produit": "Café", "prix": 3.0},
    {"categorie": "Hygiène", "produit": "Savon", "prix": 1.2},
    {"categorie": "Hygiène", "produit": "Shampooing", "prix": 3.9},
    {"categorie": "Hygiène", "produit": "Dentifrice", "prix": 2.6},
]

# Regroupement des produits par catégorie
groupes = {}
for item in catalogue:
    categorie = item["categorie"]
    groupes.setdefault(categorie, []).append(item) # Regroupe les articles par catégorie.

for categorie, items in sorted(
    groupes.items(),
    key=lambda kv: sum(x["prix"] for x in kv[1]),
    reverse=True
): # Trie les catégories par prix total décroissant.
    
    prix = sum(item["prix"] for item in items)
    print(sorted(items, key=lambda x: x["prix"], reverse=True))  # Affiche les articles triés par prix décroissant.
    log("Ex14 Total pour la catégorie " + categorie + " : " + str(prix) + "€")

# Exercice 15 - Nettoyage léger 

prenoms = [" alice ", "Bob", "ALICE", "bob ", " clara"]

def nettoyer_prenoms(prenoms):
    """
    But : Nettoie une liste de prénoms en supprimant les espaces,
    en supprimant les espaces superflus et en harmonisant en nom propre,
    puis renvoie une nouvelle liste triée des prénoms uniques dans l'ordre alphabétique.
    (première lettre majuscule, le reste en minuscule).
    """
    prenoms_nettoyes = []
    uniques = []

    for prenom in prenoms:
        propre = prenom.strip().lower().capitalize()  # Nettoie le prénom.
        prenoms_nettoyes.append(propre) # Ajoute le prénom nettoyé à la nouvelle liste.

        if propre not in uniques:
            uniques.append(propre)  # Ajoute le prénom à la liste des uniques s'il n'y est pas déjà.

    return sorted(uniques)

prenoms = nettoyer_prenoms(prenoms)
log("Ex15 Prénoms nettoyés : " + str(prenoms))

# Fermeture du fichier
fichier_resultats.close()